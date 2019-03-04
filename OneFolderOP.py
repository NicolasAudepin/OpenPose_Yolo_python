
#pic 1920 * 1080

print("__________________________________________________")
print("EXTRACTING SKELETON FROM THE KITCHEN WITH OPENPOSE")


print("\nIMPORTING LIBS")
import argparse
import logging
import time
import cv2 as cv
import numpy as np
import sys
import os
import json

print("DEFINING FUNCTIONS")
def ProssessOnePic(image):
    
    humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=resize_out_ratio)
    image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)



print("SETTING PATH")
sys.path.append('tf-openpose')
sys.path.append('tf-openpose/tf_pose')

print("SETTING CONSTS")
w=1920 #taille des images de la BDD
h=1080
resize_out_ratio = 4.0

"""
print("SETTING LOGS")
start=time.time()
logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
"""


print("SETTING THE NEURAL NETWORK")
sys.path.insert(0, '../tf-openpose')
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
e = TfPoseEstimator(get_graph_path('cmu'), target_size=(432, 368))


#this is the folder in wich all the pictures folders are
print("FOLDERS ")
kitchenDir = os.fsencode("../DATA/Cornell/kitchen")

#we try to process the pictures of each data folder
for folderNamebytes in sorted(os.listdir(kitchenDir)):
    print(folderNamebytes.strip().decode('utf-8'))

    outputfileName=folderNamebytes.strip().decode('utf-8')+".txt"
    outputDir = os.fsencode("./OPdata")

    #we try not to process the same data folder twice 
    print("is it already processed?")
    alreadyprocessed=False
    for DataNamebytes in sorted(os.listdir(outputDir)):
        #print(DataNamebytes.strip().decode('utf-8') )
        if (DataNamebytes.strip().decode('utf-8')==outputfileName):
            alreadyprocessed=True
            print("we already have a file with this name: "+DataNamebytes.strip().decode('utf-8'))
    if ( alreadyprocessed==False ):
        print("Nope !")


    #if the folder have not already been processed we process each of its image and save all of it in a txt file
    if ( alreadyprocessed==False ):
        print("INITIALIZING THE OUTPUTS")
        data={'positions':{}} #this is what will be saved as the output
        body_parts={0:"Head",1:"mShoulder",2:"rShoulder",3:"rElbow",4:"rWrist",5:"lShoulder",6:"lElbow",7:"lWrist",8:"rHip",9:"rKnee",10:"rAnkle",11:"lHip",12:"lKnee",13:"lAnkle"}

        print('THE ACTUAL PROCESSING HAPPEN HERE')
        dataDir = os.fsencode("../DATA/Cornell/kitchen/"+folderNamebytes.strip().decode('utf-8')+"/rgbjpg")
        n = 0
        for fileNamebytes in sorted(os.listdir(dataDir)):
            n = n + 1
            try: #process one image and add its skeleton to data
                print(folderNamebytes.strip().decode('utf-8')+" : "+fileNamebytes.strip().decode('utf-8'))
                fileName = fileNamebytes.strip().decode('utf-8')
                
                image = cv.imread("../DATA/Cornell/kitchen/data_01-12-07/rgbjpg/"+fileName)
                humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=resize_out_ratio) #this is the processing
                #image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
                #cv.imwrite("./OPvideos/res"+fileName,image)

                # saving the skeleton in the data if there is one
                try:
                    human=humans[0]
                    body_position={}
                    for bPart in body_parts.keys():
                        if bPart in human.body_parts:
                            x=human.body_parts[bPart].x
                            y=human.body_parts[bPart].y
                            pos=[x,y]
                            body_position[body_parts[bPart]]=pos
                    data['positions'][n]=body_position
                except:
                    print("No Skeleton on this pic?")
            except:
                print("issues with the pic ?")

        print("SAVING THE SKELETONS FILE")
        with open("./OPdata/"+folderNamebytes.strip().decode('utf-8')+".txt", 'w') as outfile:
            json.dump(data, outfile, sort_keys = True, indent = 4,ensure_ascii = False)
    else:
        print("next folder ")

print("\nTHE END")
print("__________________________________________________")

