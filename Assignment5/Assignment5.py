#Assignment 5 : Find  the  equation  of  circle  passing  through  the points (1,1),(2,−1) and (8,2).

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.set_size_inches(7,7)
ax = fig.add_subplot(111)

ax.set(xlim=(0, 10), ylim = (-3, 6))
c = plt.Circle((4.5, 1.5), radius=3.5355,ec='black',fill=None)
ax.add_artist(c)

ax.set_aspect('equal')

x=np.array([1,2,8,4.5])
y=np.array([1,-1,2,1.5])

ax.scatter(x,y,color='black')

plt.annotate("(1, 1)", (1, 1), (1.1, 1))
plt.annotate("(2, -1)", (2, -1), (2.1, -1))
plt.annotate("(8, 2)", (8, 2), (8.1, 2))
plt.annotate("(4.5, 1.5)", (4.5, 1.5), (4.6, 1.5))

ax.set_xlabel('X - axis')
ax.set_ylabel('Y - axis')
plt.show()
