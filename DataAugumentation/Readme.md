# Data Augmentation Pipeline for YOLOv7 License Plate Detection

## Overview
This repository provides a data augmentation pipeline for enhancing the YOLOv8 license plate detection model's performance. The dataset can be downloaded from [Roboflow](https://universe.roboflow.com/kanwal-masroor-gv4jr/yolov7-license-plate-detection/dataset/3).

## Setup
1. Create a virtual environment and run the command
  ```bash
pip install -r requirements.txt
```
3. Download the dataset from the provided Roboflow link.
4. Ensure the dataset follows the standard format with 'train', 'test', and 'valid' folders.

## Configuration
1. Open `main.py` in a text editor.
2. Update the `output_directory` variable (line 27) to the desired path for storing augmented images.
3. Update the `path` variable (line 57) to the path of the training images (`path='/home/user/train/*.jpg'`).
4. Repeat steps 2 and 3 for the test and valid directories in the same manner.

## Batch Processing (if dataset is huge)
If the dataset is large, modify the value of `n` (line 16) to specify the batch size for augmentation.

## Usage
Run the following command to apply augmentation:
```bash
python main.py
```
