# Pascal VOC

This folder contains code for preparing the PASCAL VOC dataset.

This README contains information about the steps and also examples for running training.

## Geting the Data

http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html

http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar

## Important Annotation Conversion

We need to convert the VOC annotations to COCO format.

We derived our code from https://github.com/yukkyo/voc2coco.git .

Our copy properly handles converting image ids to int (instead of str).

(Requires tqdm.)

```sed -e 's/$/.xml/' /path/to/data/VOCdevkit/VOC2012/ImageSets/Main/train.txt > train.txt```

```sed -e 's/$/.xml/' /path/to/data/VOCdevkit/VOC2012/ImageSets/Main/val.txt > val.txt```

```cd /path/to/data/VOCdevkit/VOC2012/Annotations```

```python3 /home/ubuntu/detr/pascalvoc/voc2coco.py --ann_paths_list /home/ubuntu/train.txt --labels /home/ubuntu/labels.txt --output /home/ubuntu/train2012.json --ext xml```

```python3 /home/ubuntu/detr/pascalvoc/voc2coco.py --ann_paths_list /home/ubuntu/val.txt --labels /home/ubuntu/labels.txt --output /home/ubuntu/val2012.json --ext xml```

## Training

make directory regular_output_dir and slotted_output_dir

```python main.py --coco_path /mnt/data/VOCdevkit/VOC2012 --epochs 100 --output_dir /home/dzhang21/detr/regular_output_dir --dataset_file pascalvoc --batch_size 10 --num_workers 12 > the_output.txt```

The slotted model takes up more memory and so it was really only feasible to use a small batch size.

```python main.py --coco_path /mnt/data/VOCdevkit/VOC2012 --epochs 100 --output_dir /home/dzhang21/detr/slotted_output_dir --dataset_file pascalvoc --batch_size 2 --num_workers 12 --slotted > the_output.txt```

## Using Pre-Extracted Features

An optional step is to convert the data by extracting the features using the SSD's VGG backbone:

https://github.com/amdegroot/ssd.pytorch

The code to extract and create the files is in the SSD_feature_extract.ipynb . Please note that without compression these total fize size can be over 16GB.

The conda YML file has been included for dependencies.

In the end we did not use this because using pre-extracted features did not give significant speedup to training.

However if you want to run the model using pre-extracted features, you can use the "identity-backbone" branch once you have created the dataset.


