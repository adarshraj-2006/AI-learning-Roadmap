# Normalize a dataset of feature values using:
import numpy as np

X = np.array([
    [20, 2000],
    [30, 3000],
    [40, 4000],
    [50, 5000]
])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

normalized = (X - mean) / std

print("Mean:", mean)
print("Standard deviation:", std)
print("Normalized data:\n", normalized)
