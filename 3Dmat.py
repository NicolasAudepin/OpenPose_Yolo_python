import scipy.io
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = scipy.io.loadmat("./data_02-10-35/depth/0001.mat")

#print(data)

mat = data["depth"]

print(mat)

plt.imshow(mat)
#plt.gray()
plt.show()