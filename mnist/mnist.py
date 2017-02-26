#% matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
from read_mnist import MNIST


# http://qiita.com/JunyaKaneko/items/b3ec906be4fb8cb713ad
class Layer:
    def __init__(self, W, b, f):
        self._W = W
        self._b = b
        self._f = f

    def propagate_forward(self, x):
        return self._f(self._W @ x + self._b)


def sigmoid(s):
    return 1 / (1 + np.exp(-1 * s))


def d_sigmoid(y):
    return y * (1 - y)


def SE(t, y):
    return ((t - y).T @ (t - y)).flatten()[0] / 2


def d_SE(t, y):
    return -(t - y)


if __name__ == "__main__":

    # 学習用のMNISTデータをインポートし、inputデータを作る
    # x: Input vector, W: Weight matrix, b: Bias, y: Output vector
    mnist = MNIST("train")

    # 単一データをインポートする場合のx作成
    x = mnist.getImage()[1].flatten()
    x = x.reshape(len(x), 1)

    # 複数のデータをインポートする場合のx作成
    # images = mnist.getImage()
    # data_num = images.shape[0]
    # images = images.reshape(data_num,-1)
    # MNISTの場合、INPUT 728 OUTPUT 10
    # for i in range(0,data_num):
    #   print(images[i].shape)

    # layer1
    n_output_1 = len(x)
    w1 = np.random.randn(n_output_1, len(x))
    b1 = np.random.randn(n_output_1, 1)
    layer1 = Layer(w1, b1, sigmoid)

    # layer2
    n_output_2 = 10
    w2 = np.random.randn(n_output_2, n_output_1)
    b2 = np.random.randn(n_output_2, 1)
    layer2 = Layer(w2, b2, sigmoid)

    # 正解のラベルをインポートし、tデータを作る(単一データの場合)
    ans = mnist.getLabel()[1]
    t = np.zeros(shape=(10, 1))
    t[ans, 0] = 1

    # 学習フェーズ
    study_rate = 0.1
    se_history = []
    delta2_history = []
    for i in range(0, 100):  # １００回学習！
        y1 = layer1.propagate_forward(x)
        y2 = layer2.propagate_forward(y1)

        se_history.append(SE(t, y2))

        delta2 = d_SE(t, y2) * d_sigmoid(y2)
        layer2._W = layer2._W - study_rate * delta2 @ y1.T
        layer2._b = layer2._b - study_rate * delta2

        delta2_history.append(np.linalg.norm(delta2))

    y1 = layer1.propagate_forward(x)
    y2 = layer2.propagate_forward(y1)

    # Draw SE history
    plt.figure()
    plt.title("SE history")
    plt.plot(range(len(se_history)), se_history)

    # Draw delta2 history
    plt.figure()
    plt.title("delta2 history")

    plt.plot(range(len(se_history)), delta2_history)

    hist_w1, bins_w1 = np.histogram(w1.flatten())
    hist_w2, bins_w2 = np.histogram(w2.flatten())

    print(y2.flatten())
    # ヒストグラムを描画
    plt.figure()
    index = range(0, 10)
    plt.title('prediction')
    plt.bar(index, y2.flatten(), align="center")
    plt.xticks(index)
    plt.show()