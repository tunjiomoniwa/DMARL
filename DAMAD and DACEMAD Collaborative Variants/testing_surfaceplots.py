import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
 
x= np.arange(-0.5,1.5,0.01)
y= np.arange(-0.5,1.5,0.01)
z= np.sin(10*x*y)

x = [6, 5, 3]
y = [3, 9, 5]
z = [4, 6, 7]
X,Y = np.meshgrid(x,y)
Z = np.sin(X*5)*np.cos(Y*5)
print(X)
print(Y)
print(Z)


fig= plt.figure()
ax= fig.add_subplot(111, projection= '3d')
surf=ax.plot_surface(X,Y,Z,cmap='afmhot',linewidth=0,antialiased='True',rstride=3,cstride=3)
ax.contourf(X, Y, Z,100, zdir='z', offset=-1.5,cmap='afmhot')
#ax.set_xlim([-0.5, 1.5])
#ax.set_ylim([-0.5, 1.5])
#ax.set_zlim([-1.5, 1.5])
fig.colorbar(surf)
plt.show()
 
