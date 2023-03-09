import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 3, 2, 1], np.float32)
y = np.array([1, 1, 2, 2, 1], np.float32)

plt.plot(x, y, "g", linewidth=1, marker="o", markersize=5)
plt.axis([0.0, 4.0, 0.0, 4.0])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")
plt.show()
