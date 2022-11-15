#many packages are building on top on numpy

#WEEK THREE JUPYTER NOTEBOOKS AND NUMPY
#GETTING STARTED WITH NDARRAY


import numpy as np



an_array=np.array([33,4,53])
print(type(an_array))
print(an_array.shape)
print(an_array[1])


an_array[0]=88
print(an_array)


#HOW TO CREATE A RANK 2 ARRAY

another=np.array([[1,2,3],[11,22,33]])
print(another)
print(another.shape)
#row first and column second

print(another[0,2])

#create a 2x2 array of zeros

example1=np.zeros((3,3))
print(example1)

#create a 2x2 array filled with 9

example2=np.full((3,3),9)
print(example2)

#create a 2x2 matrix with the diagonal 1s and the others 0

example3=np.eye(4,4)
print(example3)
#

#create an array of ones
example4=np.ones((3,5))
print(example4)

#another way to create the previous one 
example5=np.full((3,3),1)
print(example5)


#CREATE AN ARRAY OF RANDOM FLOATS BETWEEN O AND 1
example6=np.random.random((5,5))
print(example6)


#ARRAY INDEXING 


