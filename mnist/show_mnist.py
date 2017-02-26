import cv2
import numpy as np
import read_mnist as mnist


offset = 0
nx = 10
ny = 10
margin = 5

mn = mnist.MNIST("train")

#最初のoffset分を飛ばしnx*ny個の画像だけ取得
dat = mn.getImage()[offset:nx*ny+offset]

nrow, ncol = dat.shape[1:]
width = nx * (ncol+margin)+margin
height = ny * (nrow + margin)+margin
img = np.zeros((width,height), dtype = int) + 200

for iy in range(ny):
    lty = iy * (nrow + margin) +margin
    for ix in range(nx):
        ltx = ix * (ncol + margin) + margin
        img[lty:lty+nrow,ltx:ltx+ncol] = dat[iy*nx+ix]
cv2.imwrite("hoge.png", img)