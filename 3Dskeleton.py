import scipy.io
import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#loading the skeleton
with open("./OPdata/"+"data_02-10-35.txt", 'r') as skeletonData:
    skeletons = json.load(skeletonData)
    
print (skeletons[u'positions'][u'24'][u'Head'])


#loading the 3D matrice
depthData = scipy.io.loadmat("./data_02-10-35/depth/0001.mat")
depthMat = depthData["depth"]
print(depthMat)
