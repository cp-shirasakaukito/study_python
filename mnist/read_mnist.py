import struct
import numpy as np


class MNIST:
    #: train or test
    def __init__(self, type):
        if type == "train":
            self.fnLabel = 'train-labels-idx1-ubyte'
            self.fnImage = 'train-images-idx3-ubyte'
        else:
            self.fnLabel = 't10k-labels.idx1-ubyte'
            self.fnImage = 't10k-images-idx3-ubyte'

    def getLabel(self):
        return _readLabel(self.fnLabel)

    def getImage(self):
        return _readImage(self.fnImage)


# ラベルを読み込む
# return:{ ndarray[1,画像数]}
def _readLabel(fnLabel):
    f = open(fnLabel, 'rb')

    header = f.read(8)
    mn, num = struct.unpack('>2i', header)
    assert mn == 2049
    label = np.array(struct.unpack('>%dB' % num, f.read()), dtype=int)
    f.close()
    return label


# 画像を読み込む
# return{ ndarray[画像数,縦画素数,横画素数]}
def _readImage(fnImage):
    f = open(fnImage, 'rb')

    header = f.read(16)
    mn, num, rows, cols = struct.unpack('>4i', header)
    assert mn == 2051

    pixel = np.empty((num, rows, cols))
    npixel = rows * cols
    for i in range(num):
        buf = struct.unpack('>%dB' % npixel, f.read(npixel))
        pixel[i, :, :] = np.asarray(buf).reshape((rows, cols))
    f.close()
    return pixel

# mnist = MNIST("train")
# lab = mnist.getLabel()
# dat = mnist.getImage()
