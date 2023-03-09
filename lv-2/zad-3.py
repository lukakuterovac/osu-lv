import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("road.jpg")
img = img[:, :, 0].copy()
print(img.shape)

plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

plt.figure()
plt.imshow(img, cmap="gray", alpha=1)
plt.show()

img_split = img.copy()
img_split = np.hsplit(img_split, 4)
plt.figure()
plt.imshow(img_split[1], cmap="gray")
plt.show()

img_rot = np.rot90(img, 3)
plt.figure()
plt.imshow(img_rot, cmap="gray")
plt.show()

img_flip = np.fliplr(img)
plt.figure()
plt.imshow(img_flip, cmap="gray")
plt.show()
