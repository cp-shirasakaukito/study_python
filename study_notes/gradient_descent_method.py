# 勾配降下法である関数の最小値を求めよう！

import numpy as np
import matplotlib.pyplot as plt

def function_1(x):
    return x[0]**2 + x[1]**2

# 関数fのｘ1,x2における傾き
# TODO 今の仕様だと0,0に収束しないので解決する
def numerical_gradient(f, x):
    h = 1e-4
    grad = (f(x + h) - f(x - h)) / (2 * h)
    return grad

def gradient_descent(f, init_x, lr= 0.5, step_num=100):
    x = init_x
    x_transition = np.zeros([x.size,step_num+1])
    x_transition[:,0] = init_x
    for i in range(step_num):
        grad = numerical_gradient(f,x)
        x -= lr * grad
        x_transition[:,i+1] = x

    return x_transition

init_x = np.array([90.0,40.0])
X_tran = gradient_descent(function_1,init_x,0.01,200)

x = np.arange(-100,100,0.1)
y = np.arange(-100,100,0.1)

X,Y = np.meshgrid(x,y)
Z = X**2 + Y**2
plt.contour(X,Y,Z)

plt.plot(X_tran[0],X_tran[1],marker="o")

plt.colorbar()
plt.show()