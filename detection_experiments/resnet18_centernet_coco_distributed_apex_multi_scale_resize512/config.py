import os
import sys

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from public.path import COCO2017_path
from public.detection.dataset.cocodataset import CocoDetection, Resize, RandomFlip, RandomCrop, RandomTranslate, Normalize

import torchvision.transforms as transforms
import torchvision.datasets as datasets


class Config(object):
    log = './log'  # Path to save log
    checkpoint_path = './checkpoints'  # Path to store checkpoint model
    resume = './checkpoints/latest.pth'  # load checkpoint model
    evaluate = None  # evaluate model path
    train_dataset_path = os.path.join(COCO2017_path, 'images/train2017')
    val_dataset_path = os.path.join(COCO2017_path, 'images/val2017')
    dataset_annotations_path = os.path.join(COCO2017_path, 'annotations')

    network = "resnet18_centernet"
    pretrained = False
    num_classes = 80
    seed = 0
    input_image_size = 512

    use_multi_scale = True
    multi_scale_range = [0.6, 1.4]
    stride = 4

    train_dataset = CocoDetection(image_root_dir=train_dataset_path,
                                  annotation_root_dir=dataset_annotations_path,
                                  set="train2017",
                                  transform=transforms.Compose([
                                      RandomFlip(flip_prob=0.5),
                                      RandomCrop(crop_prob=0.5),
                                      RandomTranslate(translate_prob=0.5),
                                      Normalize(),
                                  ]))

    val_dataset = CocoDetection(image_root_dir=val_dataset_path,
                                annotation_root_dir=dataset_annotations_path,
                                set="val2017",
                                transform=transforms.Compose([
                                    Normalize(),
                                    Resize(resize=input_image_size),
                                ]))

    epochs = 140
    milestones = [90, 120]
    per_node_batch_size = 24
    lr = 5e-4
    num_workers = 4
    print_interval = 100
    apex = True
    sync_bn = False