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

try:
    print("dir_path = "+ dir_path)
    sys.path.append('../../')
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

print("\nTHE END")
print("_________________________________\n")
