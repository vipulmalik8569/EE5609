#Determine the distance of the point A (2, 3, 8) from the line L : x=3-2t, y=1+2t, z=-6-t .
import numpy as np

m=np.array([[-2],[2],[-1]]) # Slope vector 
p=np.array([-5,2,14]).reshape(3,1) # point p^* in affine space
u,d,vt=np.linalg.svd(m,full_matrices=True) # SVD of M
s=np.array([d[0],0,0]).reshape(3,1) 

s_plus=np.linalg.inv(s.T@s)@s.T # Moore-Pen-rose Pseudo-Inverse of s
x=vt.T@s_plus@u.T@p
print(x) #Foot of the perpendicular
print((np.linalg.inv(a.T@a))@a.T@p) #Least square solution for verification 
