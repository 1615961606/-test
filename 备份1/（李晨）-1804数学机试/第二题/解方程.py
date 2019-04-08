import numpy
import scipy.linalg as lina
#系数组成的数组（等号左边自变量的系数）
a = numpy.array([[2,1,-5,1],
                 [1,-3,0,-6],
                 [0,2,-1,2],
                 [1,4,-7,6]])
#右边的值
b = numpy.array([8,9,-5,0])
#解方程组
x = lina.solve(a,b)
print(x)