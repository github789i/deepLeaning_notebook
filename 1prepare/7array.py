import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[3, 4], [5, 6]])

print(B)
# 维数
print(np.ndim(B))
# 形状
print(B.shape)

# 矩阵乘法:点积
C = np.dot(A, B)
print(C)
