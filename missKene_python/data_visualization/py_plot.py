import numpy as np
import matplotlib.pyplot as plt

x_pt = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_pt = np.array([22, 11, 13, 55, 44, 66, 99, 88, 110, 77])

plt.xlabel('Student ID')
plt.ylabel('Student Score')

plt.plot(x_pt, y_pt, '*--r', ms=20, mec='b')

plt.xticks(x_pt)
plt.yticks(y_pt)

plt.grid(True, linestyle=':')
plt.show()