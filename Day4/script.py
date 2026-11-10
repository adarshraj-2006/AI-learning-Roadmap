import numpy as np

print("My numpy version is: ", np.__version__)

# Problem statement
# Create a NumPy program that:
# 1. Creates a 1D array containing 1 to 12.
# 2. Displays its shape, dimensions, and size.
# 3. Reshapes it into a 3 × 4 matrix.
# 4. Accesses the first row and second column.
# 5. Extracts the first two rows.
# 6. Adds 10 to every element using broadcasting.
# 7. Adds a 1D array [10, 20, 30, 40] to the matrix.
# 8. Calculates the sum and average of the matrix.

a=np.arange(1,13)
print(f"The 1D array is {a}")
print(f"The dimensions of the array is {a.ndim}")
print(f"The shape of the array is {a.shape}")
print(f"the size of the array is {a.size}")

b=a.reshape(3,4)
print(f"The reshaped 3*4 matrix is {b}")
r1=b[0,:]
c1=b[:,0]
print(f"The first row is {r1}")
print(f"The second column is {c1}")

print("\nFirst two rows:\n", b[:2])

d = np.array([10,20,30,40])
c=b+d
print("\nMatrix after adding 10 to every element:\n", c)
print("Sum:", np.sum(b))
print("Average:", np.mean(b))


# Create a 4 × 4 matrix containing numbers 1–16 and print its diagonal elements.
# Convert a 1D array of 20 elements into a 4 × 5 matrix.
# Extract the last column of a 3 × 4 matrix.
# Multiply every element of a matrix by 5 using broadcasting.
# Add a vector of 5 elements to every row of a 3 × 5 matrix.
# Calculate row-wise and column-wise sums using axis.
# Create an array of 10 student marks and calculate mean, maximum, minimum, and standard deviation.