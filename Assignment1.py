import numpy
  
u = numpy.array([1, 3, 7])  
v = numpy.array([7, 1, 8])    
  
v_mag = numpy.sqrt(sum(v**2))         
proj= (numpy.dot(u, v)/v_mag**2)*v   
  
print("Projection of Vector u on Vector v is: ", proj)
#Output : Projection of Vector u on Vector v is:  [4.05263158 0.57894737 4.63157895]
