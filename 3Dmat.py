import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = scipy.io.loadmat("./data_02-10-35/depth/0101.mat")

#print(data)

mat = data["depth"]
print(mat)


x, y = np.meshgrid(range(mat.shape[1]), range(mat.shape[0]))

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, mat)
plt.title(' mat')
plt.axis('scaled')
plt.show()

plt.imshow(mat)
#plt.gray()
plt.show()