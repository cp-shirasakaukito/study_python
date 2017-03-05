import numpy as np
import matplotlib.pyplot as plt

# 関数fのｘにおける数値微分(悪例)
# hの値が小さすぎて丸め誤差が生じるため
def numerical_diff_ng(f, x):
    h = 10e-50
    return (f(x + h) - f(x - h)) / (2 * h)

# 関数fのｘにおける数値微分
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)

# 実践1
## 数値微分から接線を出力し、接線として成立しているかをグラフで確認しよう！
def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x

def show_tangent(f,x):
    # 数値微分から接線を求める
    a1 = numerical_diff(f, x)
    b1 = f(x) - a * x

    # 出力する
    x1 = np.arange(-100,100,0.1)
    y1 = a1 * x1 + b1
    plt.plot(x1, y1)

    y2 = function_1(x1)
    plt.plot(x1, y2)
    plt.show()

### show_tangent(function_1,-79)
