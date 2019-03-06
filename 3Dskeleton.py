import scipy.io
import numpy as np
import json
import cv2 as cv

def Z(x,y,mat):
    return mat[0][0]



#loading the skeleton
with open("./OPdata/"+"data_02-10-35.txt", 'r') as skeletonData:
    skelData = json.load(skeletonData)
skeletons = skelData[u'positions']
skelist = []
for key, skeletonDict in skeletons.iteritems():
    
    skeleton=[]
    for keyleton, boneDict in skeletonDict.iteritems():
        bone=[keyleton,boneDict]
        skeleton.append(bone)
    temp = [key,skeleton]
    skelist.append(temp)

### it seems that printing too much data crash at random why?
#n=0
#m=0
#for skeleton in skelist:
#    try:
#        print (skeleton[0])
#        for bone in skeleton[1]:
#           print(bone[1])
#                
#    except:
#        print("!!!ERROR!!!")
#        print("_____________")
#        n+=1
#        try:
#            print (skeleton[0])
#            for bone in skeleton[1]:
#                print(bone[1])
#        except:
#            print("FUCKED TWICE")
#            m+=1
#print("_____________")
#print(n)
#print(m)
###


### loading the skeleton
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

for skeleton in skelist:
    frameNb= skeleton[0]
    print(frameNb)
    X=[]
    Y=[]
    for bone in skeleton[1]:
        X.append(bone[1][0])
        Y.append(bone[1][1])


    nbtxt = frameNb
    while (len(nbtxt)<4):
        nbtxt="0"+nbtxt

    #loading the 3D matrice
    depthData = scipy.io.loadmat("./data_02-10-35/depth/"+ nbtxt +".mat")
    depthMat = depthData["depth"]
    #print(depthMat)

    x, y = np.meshgrid(range(depthMat.shape[1]), range(depthMat.shape[0]))

    # show hight map in 3d
    fig = plt.figure()

    plt.subplot(2,2,1)
    plt.imshow(depthMat)
    #plt.gray()
    #plt.show()

    plt.subplot(2,2,2)
    #plot the skeleton
    plt.xlim([0,1])
    plt.ylim([1,0])
    plt.plot(X,Y,"o")
    plt.title(frameNb)
    
    plt.subplot(2,2,3)

    #im  = scipy.io.loadim("./data_02-10-35/rgbjpg/"+ nbtxt +".jpg")
    im = cv.imread('./data_02-10-35/rgbjpg/'+ nbtxt +'.jpg')

    plt.imshow(im)
    
    
    plt.show()



