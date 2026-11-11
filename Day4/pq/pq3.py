# Represent a grayscale image as a matrix. Increase brightness by 30 and extract a region of the image.

import numpy as np

image = np.array([
    [50, 100, 150, 200],
    [60, 110, 160, 210],
    [70, 120, 170, 220],
    [80, 130, 180, 230]
])

bright = np.clip(image + 30, 0, 255)

region = bright[1:3, 1:3]

print("Original image:\n", image)
print("Bright image:\n", bright)
print("Image region:\n", region)
