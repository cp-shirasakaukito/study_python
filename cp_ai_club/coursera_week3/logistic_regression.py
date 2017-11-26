import numpy as np
import matplotlib.pyplot as plt

def logistic(x,a,b):
    # log(y/(1-y)) = ax + b
    # y = np.exp(ax + b)-y(np.exp(ax + b))
    # y = np.exp(ax + b) /(1+(np.exp(ax + b))
    return np.exp(a*x + b) /(1+(np.exp(a*x + b)))

a = 0.3
b = 0.1

x = np.arange(-10,10,0.1)
b = b * np.ones(x.size)
y = logistic(x,a,b)

plt.plot(x,y)
plt.show()
