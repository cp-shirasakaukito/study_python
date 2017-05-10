# 2層のニューラルネットワークを構築
from gradient_descent_method import *
from functions import *
from study_notes.mini_batch import *
import matplotlib.pyplot as plt
import time
class twoLayerNet:
    # パラメータ初期値の定義
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(input_size,hidden_size)
        self.params["b1"] = np.zeros(hidden_size)
        self.params["W2"] = weight_init_std * np.random.randn(hidden_size,output_size)
        self.params["b2"] = np.zeros(output_size)

    # x:検証対象 ndarray[検証数:初期値で定義したinput_size]
    # y:予測結果 ndarray[検証数:初期値で定義したoutput_size]
    def predict(self, x):
        W1, W2 = self.params["W1"], self.params["W2"]
        b1, b2 = self.params["b1"], self.params["b2"]

        # 一層目はシグモイド関数
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        # 2層目はソフトマックス関数
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    # y:予測結果 ndarray[検証数、予測結果(one-hot表現)]
    # t:正解 ndarray[検証数、正答(one-hot表現)]
    # return 正解率(数値)
    def accuracy(self, y, t):
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        # 正解した数の割合を計算
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    # 損失関数
    # y:出力データ
    # t:教師データ
    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy_error(y, t)


    # y:出力データ
    # t:教師データ
    # return 傾き ndarray
    def numerical_grandient(self, x, t,):
        loss_W = lambda W: self.loss(x, t)
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        return grads

train_loss_list = []

# 数値を定義する
mini_batch_size = 100
input_size = 28 * 28
# どうやって隠れ層の数を決めるか？
hidden_layer_size = 100
output_size = 10
#繰り返し回数
iters_num = 3
learning_rate = 0.1

# 1.ミニバッチを取得
mn_train = mnist.MNIST("train")
images = mn_train.getImage(flatten=True)
labels = mn_train.getLabelMatrics()
train_size = images.shape[0]

n2 = twoLayerNet(input_size,hidden_layer_size,output_size)

for i in range(iters_num):
    #ミニバッチを取得
    batch_idx = np.random.choice(train_size, mini_batch_size)
    images_batch = images[batch_idx]
    labels_batch = labels[batch_idx]

    #勾配を取得
    grad = n2.numerical_grandient(images_batch,labels_batch)

    #パラメータ更新
    for key in ("W1", "W2", "b1", "b2"):
        n2.params[key] -= learning_rate * grad[key]

    # 学習経過の記録
    loss = n2.loss(images_batch,labels_batch)
    train_loss_list.append(loss)
    # predict = n2.predict(images_batch)
    # accuracy = n2.accuracy(predict,labels_batch)
#出力
x = np.arange(iters_num)
plt.plot(x,train_loss_list)
plt.show()