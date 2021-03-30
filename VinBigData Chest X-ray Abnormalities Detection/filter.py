import cv2
import xml.dom.minidom
import pandas as pd
import json
f=open('xxx.bbox.json','r')
dic=json.load(f)
res={}
PredictionStrings=[]
image_ids=[]
for i,ann in enumerate(dic):
    image_id=ann['image_id']
    res[image_id]=[]
for i,ann in enumerate(dic):
    image_id=ann['image_id']
    score=ann['score']
    category=ann['category_id']-1
    x1=round(ann['bbox'][0],2)
    y1=round(ann['bbox'][1],2)
    x2=round(ann['bbox'][2]+ann['bbox'][0],2)
    y2=round(ann['bbox'][3]+ann['bbox'][1],2)
    res[image_id].append([category,score,x1,y1,x2,y2])


file=open("pred.csv")
ct=0
low_thr = 0.08
high_thr =0.085
for i,line in  enumerate(file):
    if i==0:
        continue
    rs=line.strip()
    tmp,sc=rs.split(",")
    image_ids=image_ids+[tmp]
    PredictionString=""
    
    if float(sc) > low_thr:
        ct=ct+1
        for j,ann in enumerate(res[tmp]):
            if j==0:
                PredictionString=PredictionString+"{} {} {} {} {} {}".format(ann[0],ann[1],ann[2],ann[3],ann[4],ann[5])
            else:
                PredictionString=PredictionString+" {} {} {} {} {} {}".format(ann[0],ann[1],ann[2],ann[3],ann[4],ann[5])
        PredictionStrings.append(PredictionString)
    else:
        PredictionStrings.append("14 1 0 0 1 1")
    
    # if float(sc) < low_thr:
    #     PredictionStrings.append("14 1 0 0 1 1")
    # elif high_thr <= float(sc):
    #     ct=ct+1
    #     for j,ann in enumerate(res[tmp]):
    #         if j==0:
    #             PredictionString=PredictionString+"{} {} {} {} {} {}".format(ann[0],ann[1],ann[2],ann[3],ann[4],ann[5])
    #         else:
    #             PredictionString=PredictionString+" {} {} {} {} {} {}".format(ann[0],ann[1],ann[2],ann[3],ann[4],ann[5])
    #     PredictionStrings.append(PredictionString)
    # elif low_thr <= float(sc) < high_thr:
    #     PredictionStrings.append("14 {} 0 0 1 1".format(float(sc)))
    # else:
    #     raise ValueError('Prediction must be from [0-1]')
dataframe = pd.DataFrame({'image_id':image_ids,'PredictionString':PredictionStrings})
dataframe.to_csv("submission.csv",index=False)           
