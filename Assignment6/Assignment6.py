# Plot of the equation of the tangent to a circle x^2+y^2−3x+10y=15 passing through the point (4,-11).

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

u = np.array(([3/2,-5]))
f = -15
r = np.sqrt(LA.norm(u)**2-f)
x_circ= circ_gen(u,r)
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')

x=np.arange(-1,10)
y=(5/12)*x-(38/3)
plt.plot(x,y,label='$tangent$')

plt.annotate("(4, -11)", (4, -11), (4.5, -11.5))
plt.annotate("(1.5, -5)", (u[0], u[1]), (u[0]+0.2, u[1]))

plt.scatter(4,-11,color='blue')
plt.scatter(u[0],u[1],color='red')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
