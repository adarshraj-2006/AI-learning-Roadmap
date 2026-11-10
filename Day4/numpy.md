NumPy Day 4 Notes — November 5
1. Import NumPy and Check Version
import numpy as np

print("NumPy version:", np.__version__)
2. Create Arrays
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(b)
np.zeros(4)          # [0. 0. 0. 0.]
np.ones(3)          # [1. 1. 1.]
np.arange(1, 13)    # 1 to 12
np.linspace(0, 10, 5)
3. Array Properties
a = np.array([10, 20, 30, 40])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)   # (4,)
print(b.shape)   # (2, 3)
print(a.ndim)   # 1
print(b.ndim)   # 2
print(b.size)   # 6 elements
- shape: number of elements along each dimension.
- ndim: number of dimensions.
- size: total number of elements.
4. Indexing and Slicing
a = np.array([10, 20, 30, 40, 50])

print(a[0])       # 10
print(a[2])       # 30
print(a[-1])      # 50
print(a[1:4])     # [20 30 40]
b = np.array([[10, 20, 30],
              [40, 50, 60]])

print(b[0, 1])    # 20: row 0, column 1
print(b[1, 2])    # 60
print(b[0, :])     # first row
print(b[:, 1])     # second column
print(b[:, 0])     # first column
print(b[:2, :])    # first two rows
- array[row, column] accesses one 2D element.
- : selects all elements along that axis.
- Indexing starts from 0.
5. Reshape Arrays
a = np.arange(1, 13)
b = a.reshape(3, 4)

print(a)
print(b)
print(b.shape)     # (3, 4)
The total element count must remain unchanged: 12 = 3 × 4.
a.reshape(2, 6)    # valid
a.reshape(4, 3)    # valid
# a.reshape(3, 5)   # invalid: element count differs
6. Broadcasting
Broadcasting applies operations between compatible array shapes.
Scalar broadcasting
a = np.array([10, 20, 30])

print(a + 5)       # [15 25 35]
print(a * 2)       # [20 40 60]
Vector broadcasting across matrix rows
b = np.array([[1, 2, 3],
              [4, 5, 6]])

v = np.array([10, 20, 30])

print(b + v)
# [[11 22 33]
#  [14 25 36]]
For broadcasting, dimensions are compatible when they are equal or one of them is 1.
7. Array Operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)       # [11 22 33]
print(a - b)       # [ 9 18 27]
print(a * b)       # [10 40 90]
print(a / b)       # [10. 10. 10.]

print(np.sum(a))   # 60
print(np.mean(a))  # 20.0
print(np.max(a))   # 30
print(np.min(a))   # 10
8. Axis Operations
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.sum(b, axis=0))  # column-wise: [5 7 9]
print(np.sum(b, axis=1))  # row-wise: [6 15]
print(np.mean(b, axis=0)) # column-wise average
print(np.mean(b, axis=1)) # row-wise average
- axis=0: operate down rows; result is column-wise.
- axis=1: operate across columns; result is row-wise.
9. Practical Task — Complete Program
import numpy as np

print("NumPy version:", np.__version__)

# 1. Create a 1D array from 1 to 12
a = np.arange(1, 13)
print("1D array:", a)

# 2. Display properties
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Size:", a.size)

# 3. Reshape into 3 x 4
b = a.reshape(3, 4)
print("Matrix:\\n", b)

# 4. First row and second column
print("First row:", b[0, :])
print("Second column:", b[:, 1])

# 5. First two rows
print("First two rows:\\n", b[:2, :])

# 6. Add 10 using scalar broadcasting
print("Add 10:\\n", b + 10)

# 7. Add vector using broadcasting
v = np.array([10, 20, 30, 40])
print("Add vector:\\n", b + v)

# 8. Sum and average
print("Sum:", np.sum(b))
print("Average:", np.mean(b))

# Extra: row-wise and column-wise sums
print("Column sums:", np.sum(b, axis=0))
print("Row sums:", np.sum(b, axis=1))