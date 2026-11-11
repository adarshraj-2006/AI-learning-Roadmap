# Analyze sales of 3 products across 4 months.
# Calculate total sales per product, monthly sales, and apply a 10% price increase.

import numpy as np

sales = np.array([
    [100, 120, 150, 180],
    [200, 220, 250, 280],
    [150, 170, 190, 210]
])

print("Product sales:", np.sum(sales, axis=1))
print("Monthly sales:", np.sum(sales, axis=0))

increased = sales * 1.10

print("After 10% increase:\n",increased)