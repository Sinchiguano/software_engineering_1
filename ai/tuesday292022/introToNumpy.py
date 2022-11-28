#GETTING STARTED WITH ARRAYS
#HOW TO CREATE RANK 1 NUMPY ARRAY


import numpy as np


ex1=np.array([1,2,3])
print(ex1)
print(type(ex1))
print(ex1.shape)
#because this is a 1-rank array, we need only one index to access each element
print(f'This is a 1-rank array \n{ex1}')
print("##############")


#ndarray are mutable
ex1[1]=888
print(ex1)


print("##############")
#HOW TO CREATE A RANK 2 NUMPY ARRAY
ex2=np.array([[1,2,3],[11,22,33]])
print(ex2)


print("The shape is 2 row and 2 columns",ex2.shape)
print("Accessing element [0,0], [1,1],[1,2]",ex2[0,0], "-" ,ex2[1,1], "-",ex2[1,2])


print("##############")
#THERE ARE MANY WAYS TO CREATE NUMPY ARRAY

#CREATE A 2X2 ARRAY OF ZEROS
ex3=np.zeros((2,2))
print(ex3)
ex4=np.zeros((5,5))
print(ex4)
#CREATE A 3X3 FILLED WITH 9.0
ex5=np.full((3,3),9.0)
print(ex5)
#CREATE A 5X5 MATRIX WITH THE DIAGONAL 1S AND THE OTHERS 0
ex6=np.eye(5,5)
print(ex6)

#CREATE ARRAY OF RANDOM FLOATS BETWEEN 0 AND 1
ex7=np.random.random((3,3))
print(ex7)
