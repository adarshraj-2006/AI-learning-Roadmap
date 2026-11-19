# Calculate the dot product of two arrays using loops and np.dot().
# Multiply two 3×3 matrices using loops and @.
# Compare element-wise multiplication and matrix multiplication.
# Transpose a matrix and calculate its determinant.
# Generate two 200×200 matrices and compare loop-based multiplication with NumPy timing.
import numpy as np
a=[1,4,2,5,3]
b=[6,9,7,10,8]

def dot_prod(a,b):
    return np.dot(a,b)
print(f"Dot Product: {dot_prod(a,b)}")

Matrix1= np.array([[1,2,3],[4,2,3],[3,3,4]])
Matrix2= np.array([[1,5,8],[8,7,9],[3,3,4]])
def matrix_mult(Matrix1,Matrix2):
    return Matrix1 @ Matrix2
print(f"Matrix Multiplication:\n{matrix_mult(Matrix1,Matrix2)}")

result = np.zeros((3, 3))

print(f"Dot Product:\n{result}")
result = np.zeros((3, 3), dtype=int)

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += Matrix1[i][k] * Matrix2[k][j]
print(f"Matrix Multiplication:\n{result}")

t=result.T
print(f"Transpose of the Matrix:\n{t}")
d = np.linalg.det(Matrix1)
print(f"Determinant of the Matrix:\n{d}")

# matrix multiplication 
# The objective of this question is to 
# understand why NumPy performs matrix multiplication faster than normal Python loops.
import numpy as np
import time

a=np.random.rand(200,200)
b=np.random.rand(200,200)
start=time.perf_counter()

#  using python loops
result1 = [[0.0 for j in range(200)] for i in range(200)]

for i in range(200):
    for j in range(200):
        for k in range(200):
            result[i][j] +=a[i][k]*b[k][j]
        
    

end=time.perf_counter()
loop_time=start-end

# using numpy
start=time.perf_counter()
result2=a @ b
end=time.perf_counter()

numpy_time=start-end

print("Loop execution time:", loop_time)
print("NumPy execution time:", numpy_time)

print("Results match:", np.allclose(result1, result2))

print("Speedup:", loop_time / numpy_time, "times")

