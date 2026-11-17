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

