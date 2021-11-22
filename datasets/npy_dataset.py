# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
"""
COCO dataset which returns image_id for evaluation.

Mostly copy-paste from https://github.com/pytorch/vision/blob/13b35ff/references/detection/coco_utils.py
"""
from pathlib import Path

import torch
import torch.utils.data
import torchvision
from pycocotools.coco import COCO

import datasets.transforms as T

import numpy as np

class CocoDetection(torch.utils.data.Dataset):
    """
    https://github.com/pytorch/vision/blob/main/torchvision/datasets/coco.py
    """

    def __init__(
        self,
        root: str,
        annFile: str
    ) -> None:
        super().__init__()

        self.root = root
        self.coco = COCO(annFile)
        self.ids = list(sorted(self.coco.imgs.keys()))

    def _load_image(self, id: int):
        path = self.coco.loadImgs(id)[0]["file_name"]
        return np.load(os.path.join(self.root, path[:-3] + 'npy'))

    def _load_target(self, id: int):
        return self.coco.loadAnns(self.coco.getAnnIds(id))

    def __getitem__(self, index: int):
        id = self.ids[index]
        image = self._load_image(id)
        target = self._load_target(id)

        return image, target

    def __len__(self) -> int:
        return len(self.ids)

def build(image_set, args):
    root = Path(args.coco_path)
    assert root.exists(), f'provided COCO path {root} does not exist'

    PATHS = {
        "train": (root / "JPEGImages", root / "annotations" / f'train2012.json'),
        "val": (root / "JPEGImages", root / "annotations" / f'val2012.json'),
    }

    img_folder, ann_file = PATHS[image_set]
    dataset = CocoDetection(img_folder, ann_file)
    return dataset
