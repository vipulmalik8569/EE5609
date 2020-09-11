import numpy as np
m=int(input("Enter number of rows    :"))
n=int(input("Enter number of columns :"))
matrix=[]
for i in range(m):
  for j in range(n):
    matrix.append(int(input("Enter {} X {} element of your matrix :".format(i+1,j+1))))

mat_1=np.array(matrix,dtype=float).reshape(m,n)
mat_2=mat_1  
E_matrix=np.identity(m)    #Elimination matrix initialisation
print("Matrix that you have entered is :\n",mat_2)
for k in range(n-1):
  I1=np.identity(m,dtype=float) 
  if mat_2[k][k]==0:
    I2=np.identity(m,dtype=float)
    I2[[k,k+1]]=I2[[k+1,k]]        # This creates a Permutation matrix by swapping the rows of identity matrix.
    mat_2 = I2 @ mat_2            
  I1[k+1:m,k]=mat_2[k+1:m,k]/(-mat_2[k][k]) # This creates the Elimination matrix   
  E_matrix= I1 @ E_matrix          # This gives the repeated product of elimination matrices.
  mat_2 = I1 @ mat_2        # This performs the row tranformations on mat_2 and finally give reduced row echelon form of matrix.

print("Row reduced echelon form of your matrix is :\n",mat_2)
if n==m:
  if np.linalg.det(mat_1):
    for l in range(n-1):
      I1=np.identity(m,dtype=float)
      I1[0:m-1-l,n-1-l]=mat_2[0:m-1-l,n-1-l]/(-mat_2[m-1-l][m-1-l])  # This creates the Elimination matrix for further reduction.
      E_matrix= I1 @ E_matrix  
      mat_2 = I1 @ mat_2            #This performs the row tranformations on mat_2 and finally give a diagonal matrix.
    for x in range(m):
      for y in range(n):
        if x==y:
          E_matrix[x][y]/= mat_2[x][y]  # This gives the inverse after dividing all the diagonal elements of E_matrix by diagonal elements of mat_2. 
    print("Inverse of your matrix is : \n",E_matrix)
  else:
    print("Your matrix is singular.") 
else :
  print("Your matrix is rectangular.") 
