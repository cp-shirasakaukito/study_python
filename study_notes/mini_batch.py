import read_mnist as mnist
import numpy as np

# 60000枚の訓練データの中からnumber枚をランダムで選び出し
# そのインデックスをndarrayで返却する
def get_mini_batch_idx(number):
    # 60000枚の訓練データの中から100枚をランダムで選び出す
    mn = mnist.MNIST("train")
    images = mn.getImage()
    labels = mn.getLabelMatrics()

    # インデックスをランダムで取得
    train_size = images.shape[0]
    batch_size = number
    batch_idx = np.random.choice(train_size, batch_size)

    return batch_idx