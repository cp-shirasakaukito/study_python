import sys, os
sys.path.append(os.curdir + "/deep-learning-from-scratch")
import numpy as np
from dataset.mnist import load_mnist

#評価する１
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle