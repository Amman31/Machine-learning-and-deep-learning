import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale
image = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)

# Define the 3x3 vertical Sobel filter
sobel_vertical = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

sobel_horizontal = np.array([[-1, -2, -1],
                             [0, 0, 0],
                             [1, 2, 1]])

vertical_edges = cv2.filter2D(image, -1, sobel_vertical)
horizontal_edges = cv2.filter2D(image, -1, sobel_horizontal)

# Display the original and the edge-detected images
plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)  # Adjusted to create three subplots
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Vertical edge-detected image
plt.subplot(1, 3, 2)  # Second subplot for vertical edges
plt.imshow(vertical_edges, cmap='gray')
plt.title('Vertical Edges')
plt.axis('off')

# Horizontal edge-detected image
plt.subplot(1, 3, 3)  # Third subplot for horizontal edges
plt.imshow(horizontal_edges, cmap='gray')
plt.title('Horizontal Edges')
plt.axis('off')

plt.show()
