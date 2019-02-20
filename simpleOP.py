
#pic 1920 * 1080

print("_________________________________")
print("EXTRACTING SKELETON FROM OPENPOSE")


print("\nIMPORTING LIBS")
import argparse
import logging
import time
import cv2 as cv
import numpy as np
import sys
import os
import json

print("SETTING PATH")
sys.path.append('tf-openpose')
sys.path.append('tf-openpose/tf_pose')

print("SETTING CONSTS")
w=5472
h=3648
resize_out_ratio = 4.0

print("SETTING LOGS")
start=time.time()
logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

print("CHOOSING THE PIC")
image = cv.imread("test.jpg")

print("SETTING THE NEURAL NETWORK")
sys.path.insert(0, '../tf-openpose')
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
#logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
e = TfPoseEstimator(get_graph_path('cmu'), target_size=(432, 368))

print('THE ACTUAL PROCESSING HAPPEN HERE')

humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=resize_out_ratio)
image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

print("SAVING THE STUFF")

cv.imwrite("result.jpg",image)
data={'positions':{}}
human=humans[0]

    body_position={}
    body_parts={0:"Head",1:"mShoulder",2:"rShoulder",3:"rElbow",4:"rWrist",5:"lShoulder",6:"lElbow",7:"lWrist",8:"rHip",9:"rKnee",10:"rAnkle",11:"lHip",12:"lKnee",13:"lAnkle"}
    for bPart in body_parts.keys():
        if bPart in human.body_parts:
            x=human.body_parts[bPart].x
            y=human.body_parts[bPart].y
            pos=[x,y]
            body_position[body_parts[bPart]]=pos
    data['positions'][duration]=body_position
     with open("%s/dataOP/skeleton.txt"%args.save_data, 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4,ensure_ascii = False)


print("\nTHE END")
print("_________________________________\n")
