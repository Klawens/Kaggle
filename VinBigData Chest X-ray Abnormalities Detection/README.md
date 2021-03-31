## VinBigData Chest X-ray Abnormalities Detection
### Automatically localize and classify thoracic abnormalities from chest radiographs
### 2020-12-31 UTC+8
#### It's a object detection game!

### Data format:
#### test image: 3000 xxx.dicom
#### train image: 15000 xxx.dicom
#### train.csv has more than 67000 data of 15 class(No finding included)

### Used scripts to format the dataset to coco, scripts in another repository 'dataset_prepare'.
#### 'img2csv.py' 'csv2coco.py'

#### Final Score Public LB: 0.289(Silver)
####             Private LB: 0.254(Bronze)
