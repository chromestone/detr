# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from .detr import build


def build_slottedmodel(args):
    return build(args)
