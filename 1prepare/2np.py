import numpy as np

A = np.array([[1, 2], [3, 4], [0, 4]])
print(A)
print(A.shape) #(3, 2)
print(A.dtype) #int32

# 访问元素
print(A[0]) #[1 2]
print(A[0][1]) #2

for row in A:
    print(row)

A = A.flatten()
print(A) #[1 2 3 4 0 4]
print(A[np.array([0,2,4])]) #[1 3 0]

print(A > 1) #[False  True  True  True False  True]
print(A[A>1]) #[2 3 4 4]


# 矩阵运算
# @表示常规的数学上定义的矩阵相乘；*表示两个矩阵对应位置处的两个元素相乘
X = np.array([[1, 3], [5, 0]])
Y = np.array([[2, 8], [1, 2]])
print(X*Y)
print(X@Y)

# 广播 broadcast
print(X*10)

Z = np.array([10, 10])
print(X*Z)