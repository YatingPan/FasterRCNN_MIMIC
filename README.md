# Object Detector for Chest Imagenome Dataset

This repository contains the processing and training scripts for an object detector based on Faster R-CNN, specifically for the Chest Imagenome dataset.

## Overview

The object detector is trained, evaluated, and tested on the Chest Imagenome dataset. The dataset comprises 29 anatomical regions extracted from the MIMIC-CXR image dataset for object detection.

## Prerequisites

To use this repository, ensure the following datasets are prepared:

1. **Chest Imagenome**: Utilize the scene graph folder of the silver datasets, which contains JSON files detailing 29 anatomical regions with bbox coordinates and attributes.
2. **MIMIC-CXR JPG Dataset**: Provides images for the Chest Imagenome.
3. **MIMIC-CXR Reports Dataset**: Generates train, test, and validation datasets for subsequent vision-language model frameworks.

## Data Processing

Scripts under `object_detector/src/dataset` are used for processing and creating datasets:

### Constants and Faulty Data Identification

- `constants.py`: Stores 29 regions defined by the Chest Imagenome dataset and images to be ignored due to detection failure.
- `identify_faulty_data.py`: Detects faulty bounding boxes (bboxes) in the Chest Imagenome dataset. Outputs include `faulty_bbox_coordinates.csv` and `faulty_bbox_names.csv` for bboxes with incorrect dimensions or labels.

### Dataset Statistics and Creation

- `compute_stats_dataset.py`: Counts data in the Chest Imagenome dataset, like the proportion of abnormal bboxes, correspondence between bboxes and phrases, etc.
- `create_dataset_new.py`: Generates CSV files for train, validation, and test datasets, excluding detected faulty bboxes. The train dataset CSV includes subject_id, study_id, image_id, path, bbox_coordinates, bbox_labels, bbox_phrases, bbox_phrases_exists, and bbox_is_abnormal. Validation and test datasets also include the corresponding `report`.

## Object Detector Based on Faster R-CNN

Scripts in `object_detector/src/object_detector` are based on PyTorch's Faster R-CNN with modifications for the Chest Imagenome dataset:

- `image_list.py`: Adjusted to handle the consistent image size (256×256) of the MIMIC-CXR JPG images.
- `rpn.py` and `roi_heads.py`: Modified to add loss calculation during evaluation.
- `object_detector.py`: Tailored for the Chest Imagenome dataset.
    - Uses a ResNet50 model pre-trained on chest x-rays.
    - Accepts grayscale images (1 channels instead of 3).
    - The backbone ends before the final two layers (AdaptiveAvgPool2d and Linear) of the standard ResNet50, focusing only on feature extraction.
    - Expects tensors of shape [batch_size, 1, H, W], where H and W are typically 512.
- `training_script_object_detector.py`: Script for training and evaluating the object detector. Outputs include a "runs" folder for saving checkpoints.

## Usage

1. Set up the paths for the dataset and training output checkpoints in `object_detector/src/path_datasets_and_weights.py`.
2. Follow the instructions in each script under the `object_detector/src/dataset` and `object_detector/src/object_detector` directories.
