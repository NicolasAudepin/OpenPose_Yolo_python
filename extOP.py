#heavily inspired by https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/examples/tutorial_api_python/2_whole_body_from_image.py


print("_________________________________")
print("EXTRACTING SKELETON FROM OPENPOSE")


print("importing libs")
import sys
import cv2
import os
from sys import platform
import argparse


print("setting the paths")
dir_path = os.path.dirname(os.path.realpath(__file__))
print("dir_path = "+ dir_path)

try:
    
    sys.path.append('../../')
    sys.path.append('../../')
    print("importing openpose as op")
    from openpose import pyopenpose as op
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

# 
params = dict()
params["model_folder"] = "../../../models/"
params["face"] = True
params["hand"] = True
print(params)


#Starting OP
print('creating OPWraper')
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()



print("\nTHE END")
print("_________________________________\n")
