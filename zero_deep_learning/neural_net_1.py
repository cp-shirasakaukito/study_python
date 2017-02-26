import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x,w,b):
    return 1/(1+np.exp(-(np.dot(x,w) + b)))

def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y

def init_network():
    network = {}
    network["W1"] = np.array([[0.1,0.2,0.3],[0.4,0.5,0.6]])
    network["b1"] = np.array([0.1,0.2,0.3])
    network["W2"] = np.array([[0.1,0.2],[0.4,0.5],[0.7,0.8]])
    network["b2"] = np.array([0.1,0.2])
    network["W3"] = np.array([[0.1,0.2],[0.4,0.5]])
    network["b3"] = np.array([0.1,0.2])
    return network

network = init_network()
x = np.array([0.1, 0.3])
y1 = sigmoid(x,network["W1"],network["b1"])
y2 = sigmoid(y1,network["W2"],network["b2"])
y3 = sigmoid(y2,network["W3"],network["b3"])

a = np.array([0.3,2.9,4.0])
exp_a = np.exp(a)
print()
