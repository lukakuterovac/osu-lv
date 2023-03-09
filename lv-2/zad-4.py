import matplotlib.pyplot as plt
import numpy as np

zero = np.zeros((50, 50))
one = 255 * np.ones((50, 50))

row1 = np.hstack((zero, one))
row2 = np.hstack((one, zero))

img = np.vstack((row1, row2))
plt.figure()
plt.imshow(img, cmap="gray")
plt.show()
