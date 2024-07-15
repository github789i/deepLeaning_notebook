import numpy as np


# 与门，权重 w 是控制输入信号的重要性的参数，偏置 b 决定了神经元被激活的容易程度
def AND(x1, x2):
    x = np.array(x1, x2)
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 与非门
def NAND(x1, x2):
    x = np.array(x1, x2)
    w = np.array([-0.5, -0.5])  # 仅权重和偏置与AND不同
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 或门
def OR(x1, x2):
    x = np.array(x1, x2)
    w = np.array([0.5, 0.5])  # 仅权重和偏置与AND不同
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 异或门使用组合感知机实现
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y