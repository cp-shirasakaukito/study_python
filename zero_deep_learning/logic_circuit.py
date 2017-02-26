import numpy as np

x11 = np.array([1,1])
x10 = np.array([1,0])
x01 = np.array([0,1])
x00 = np.array([0,0])

def perceptron(x,w,b):
    tmp = np.dot(x,w.T)
    if tmp > b:
        return 1
    elif tmp <= b:
        return 0

def p_and(x):
    and_w = np.array([0.5, 0.5])
    and_b = 0.8
    return perceptron(x, and_w, and_b)
def p_or(x):
    or_w = np.array([0.5, 0.5])
    or_b = 0.3
    return perceptron(x, or_w, or_b)
def p_nand(x):
    nand_w = np.array([-0.5, -0.5])
    nand_b = -0.8
    return perceptron(x,nand_w,nand_b)
def p_xor(x):
    or_result = p_or(x)
    nand_result = p_nand(x)
    inter = np.array([or_result,nand_result])
    xor_result = p_and(inter)
    return xor_result
print("AND")
print(p_and(x11))
print(p_and(x01))
print(p_and(x10))
print(p_and(x00))
print("OR")
print(p_or(x11))
print(p_or(x01))
print(p_or(x10))
print(p_or(x00))
print("NAND")
print(p_nand(x11))
print(p_nand(x01))
print(p_nand(x10))
print(p_nand(x00))

print("XOR")
print(p_xor(x11))
print(p_xor(x01))
print(p_xor(x10))
print(p_xor(x00))

