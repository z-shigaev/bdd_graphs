# importing cursor widget from matplotlib
from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

num = 100
x = np.random.rand(num)
y = np.random.rand(num)

ax.scatter(x, y, c='blue')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

cursor = Cursor(ax, color='green', linewidth=2)
plt.show()
