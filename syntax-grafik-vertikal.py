import numpy as np
from matplotlib import pyplot as plt
x=(2012, 2013, 2014, 2015, 2016)
y=(1005, 900, 2050, 2000, 800)
plt.figure(figsize=(10,5))
plt.bar(x,y)
#plt.grid()
plt.show()