import numpy as np
from PIL import Image
import read_mnist as mnist

#

offset = 50
nx = 10
ny = 10
margin = 5

mn = mnist.MNIST("train")

# 最初のoffset分を飛ばしnx*ny個の画像だけ取得して、
# 結合して画像として出力するプログラム
dat = mn.getImage()[offset:nx*ny+offset]

# 始めの１画像だけ取り出して縦横の画素数を取得
nrow, ncol = dat.shape[1:]

# 出力する画像の画素数を計算し、下地を作る
width = nx * (ncol+margin)+margin
height = ny * (nrow + margin)+margin
img = np.zeros((width,height), dtype = int) + 200

# 作成した下地にmnist画像をはめ込んでいく
for iy in range(ny):
    lty = iy * (nrow + margin) +margin
    for ix in range(nx):
        ltx = ix * (ncol + margin) + margin
        img[lty:lty+nrow,ltx:ltx+ncol] = dat[iy*nx+ix]
images = np.asarray(img,np.uint8) # 注）fromarrayで表示するにはuint8じゃないとdatatypeエラーになった
# 行列を画像として出力する
pilOUT = Image.fromarray(images)
pilOUT.show()