#Find the QR decomposition of the matrix V.
import numpy as np

V=np.array([[1, 1/2],[1/2 , 1]]) #Input matrix

Q,R=np.linalg.qr(V)
print(V)
print(Q)    #Orthogonal matrix
print(R)    #Upper triangular matrix
print(Q@R)  #For Verification
