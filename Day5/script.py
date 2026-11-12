# Topics: Vectorization, dot product, matrix multiplication, matrix operations, loops vs NumPy performance.

import numpy as np
import time

# Dot product using Python loops
def dot_loop(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i] * b[i]

    return result

# Dot product using NumPy
def dot_numpy(a, b):
    return np.dot(a, b)


a = np.array([2, 3, 4])
b = np.array([5, 6, 7])

print("Loop dot:", dot_loop(a, b))
print("NumPy dot:", dot_numpy(a, b))

# Matrix multiplication using loops
def matrix_loop(A, B):
    rows = A.shape[0]
    cols = B.shape[1]
    common = A.shape[1]

    result = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            for k in range(common):
                result[i, j] += A[i, k] * B[k, j]

    return result


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Loop matrix:\n", matrix_loop(A, B))
print("NumPy matrix:\n", A @ B)

# Timing comparison
A = np.random.rand(200, 200)
B = np.random.rand(200, 200)

start = time.perf_counter()
matrix_loop(A, B)
loop_time = time.perf_counter() - start

start = time.perf_counter()
A @ B
numpy_time = time.perf_counter() - start

print("Loop time:", loop_time)
print("NumPy time:", numpy_time)
print("Speedup:", loop_time / numpy_time)
