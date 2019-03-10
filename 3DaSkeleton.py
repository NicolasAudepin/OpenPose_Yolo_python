import scipy.io
import numpy as np
import json
import cv2 as cv

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def tronc(x,len):
    ret = 0
    if (x<2):
        ret = 2
    if (x>len-2):
        ret = len-2
    else:
        ret = x
    return ret

def ZfromMat(x,y,mat):
    xlen=len(mat)
    ylen=len(mat[0])
    xmat = int(round(x*xlen))-50
    ymat = int(round(y*ylen*1.25))-190

    #print(xmat)
    #print(ymat)

    xmat=int(tronc(xmat,xlen))
    ymat=int(tronc(ymat,ylen))
    z=mat[xmat][ymat]
    
    return [z,xmat,ymat]



#loading the skeleton from the file
with open("./OPdata/"+"data_02-10-35.txt", 'r') as skeletonData:
    skelData = json.load(skeletonData)
skeletons = skelData[u'positions']

running = True
nb = "0"
while(running):
    inputTxt=input("next one ?")
    keyboard = str(inputTxt)
    if (keyboard==""):
        print("next")
        nb = str(int(nb)+1)
    if(keyboard=="x"):
        running = False
        
    if(len(keyboard)<5):
        nb = int(keyboard)
    else:
        print("try again")
    #print(str(nb)+"NB")
    nbtxt = keyboard
    while (len(nbtxt)<4):
        nbtxt="0"+nbtxt

    #exctract the key point list from the skeleton
    skeletonDict= skeletons[str(nb)]
    skeleton=[]
    for keyleton, boneDict in skeletonDict.iteritems():
        bone=[keyleton,boneDict]
        skeleton.append(bone)
    X=[]
    Y=[]
    Z=[]
    for bone in skeleton:
        X.append(bone[1][0])
        Y.append(bone[1][1])



    depthData = scipy.io.loadmat("./data_02-10-35/depth/"+ nbtxt +".mat")
    depthMat = depthData["depth"]
    
    #draw the skeleton over the depth picture
    for bone in skeleton:
        z,xmat,ymat=ZfromMat(bone[1][1],bone[1][0],depthMat)
        Z.append(z)
        depthMat[xmat][ymat]=9000
        depthMat[xmat-1][ymat]=9000
        depthMat[xmat+1][ymat]=9000
        depthMat[xmat][ymat-1]=9000
        depthMat[xmat][ymat+1]=9000
        depthMat[xmat+1][ymat-1]=9000
        depthMat[xmat+1][ymat+1]=9000
        depthMat[xmat-1][ymat-1]=9000
        depthMat[xmat-1][ymat+1]=9000
    
    
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
    plt.title(nbtxt)
    
    plt.subplot(2,2,3)

    #im  = scipy.io.loadim("./data_02-10-35/rgbjpg/"+ nbtxt +".jpg")
    im = cv.imread('./data_02-10-35/rgbjpg/'+ nbtxt +'.jpg')

    plt.imshow(im)

    ax = fig.add_subplot(224, projection='3d')
    ax.set_xlim(0,1)
    ax.set_zlim(1,0)
    ax.scatter(X,Z,Y)
    
    
    plt.show()



