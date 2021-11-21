# Pascal VOC

This folder contains code for preparing the dataset.

(Requires tqdm.)

```git clone https://github.com/yukkyo/voc2coco.git```

```sed -e 's/$/.xml/' /path/to/data/VOCdevkit/VOC2012/ImageSets/Main/train.txt > train.txt```

```sed -e 's/$/.xml/' /path/to/data/VOCdevkit/VOC2012/ImageSets/Main/val.txt > val.txt```

```cd /path/to/data/VOCdevkit/VOC2012/Annotations```

```python3 /home/ubuntu/voc2coco/voc2coco.py --ann_paths_list /home/ubuntu/train.txt --labels /home/ubuntu/labels.txt --output /home/ubuntu/train2012.json --ext xml```

```python3 /home/ubuntu/voc2coco/voc2coco.py --ann_paths_list /home/ubuntu/val.txt --labels /home/ubuntu/labels.txt --output /home/ubuntu/val2012.json --ext xml```
