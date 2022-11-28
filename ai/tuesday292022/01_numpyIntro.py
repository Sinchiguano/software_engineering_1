print("Hello world")

#BASICS OF WORKING WITH ARRAYS
#DATA STRUCTURE

import numpy as np
an_array=np.array([3,33,333])
print(an_array)
print(type(an_array))

an_array[1]=888
print(an_array)


#HOW TO CREATE A RANK 2 NUMPY ARRAY
import numpy as pablito

tmp=pablito.array([[1,2,3],
                 [11,22,33]])
print(tmp)


#THERE ARE MANY WAY TO CREATE NUMPY ARRAYS
print("*************************")
import numpy as np

#create a 2x2 array of zeros
ex1=np.zeros((2,2))
print(ex1)

ex1=np.zeros((4,2))
print(ex1)
#create a 2x2 array filled with 9
ex2=np.full((2,2),9)
print(ex2)
#create a 2x2 matrix with the diagonal 1s and the others 0
ex3=np.eye(3,3)
print(ex3)


print("*************************")
#create an array of ones
ex4=np.ones((3,3))
print(ex4)
print(ex4.shape)

#create an array of random floats between 0 and 1
ex5=np.random.random((2,2))
print(ex5)









