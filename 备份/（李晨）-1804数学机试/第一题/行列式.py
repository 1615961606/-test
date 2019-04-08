import numpy as np
from numpy.linalg import*
#行列式a
a = np.array([[3,1,-1,2],
             [-5,1,3,-4],
             [2,0,1,-1],
             [1,-5,3,-3]])
print(det(a))#求a的行列式的值

b = np.array([[-2,-1,1,-2],
             [5,0,-3,4],
             [-2,0,0,1],
             [-1,5,-3,4]])
print(det(a))#求b的行列式的值