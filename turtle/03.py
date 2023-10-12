import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,1,1,1,1,1,1,1,1,1]

colours = [1,2,3,4,5,6,7,8,9,10]

plt.scatter(x,y, s = 100 , c = colours, cmap = 'bwr' )
plt.colorbar(orientation = "horizontal")
plt.show()