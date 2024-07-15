import numpy as np
import matplotlib.pyplot as plt


# 阶跃函数：判断数组x是否满足条件得到bool型数组，再根据bool值通过dtype属性返回int型数组
def step_function(x):
    return np.array(x > 0, dtype=np.int32)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)
y3 = relu(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.ylim(-0.1, 2)
plt.show()
