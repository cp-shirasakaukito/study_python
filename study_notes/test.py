from functions import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def function_2(x,y):
    return x**2 + y**2

x = np.arange(-100, 100, 4)
y = np.arange(-100, 100, 4)
X,Y = np.meshgrid(x,y)
Z = function_2(X,Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z)

plt.show()
