
#FINAL PROLJECT
#LATEX INFORMATION ABOUT TEMPLATE OF JOURNAL ARTICLES
#https://www.overleaf.com/gallery/tagged/academic-journal/page/3
#https://github.com/Sinchiguano/nothing/blob/master/inf/spamFilter.pdf



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

print("##############")
#ARRAY INDEXING
#SLICE INDEXING
##RANK 2 ARRAY OF SHAPE (3,4)
ex8=np.array([[11,12,13,14],
              [21,22,23,24],
              [31,32,33,34]])
print(ex8.shape)
print("Before ex8 array: \n",ex8)
print("##############")
newArray=ex8[0:2,1:3]
print(newArray)
newArray[1,1]=77
print(ex8)

print("After ex8 array: \n",newArray)



print("##############")
#COPY ARRAY
ex8=np.array([[11,12,13,14],
              [21,22,23,24],
              [31,32,33,34]])
print("Before ex8 array: \n",ex8)

ex8_copy=ex8.copy()
newArray=ex8_copy[0:2,1:3]
newArray[1,1]=77
print("After ex8 array: \n",ex8_copy)

print("##############")


#USE BOTH INTEGER INDEXING AND SLICE INDEXING

ex9=np.array([[11,12,13,14],
              [21,22,23,24],
              [31,32,33,34]])
ex9_slicing=ex9[1,:]
print(ex9_slicing.shape)

#WE CAN DO THE SAME THING FOR COLUMNS OF AN ARRAY
col_rank2=ex9[:,1:2]
print(col_rank2.shape)

print("##############")
#SOMETIME IT IS USEFUL TO USE AN ARRAY OF INDEXES TO ACCESS OR CHANGE ELEMENTS
ex10=np.array([[11,12,13,14],
              [21,22,23,24],
              [31,32,33,34],
              [41,42,43,44]])
print("ORIGINAL ARRAY")        
print(ex10)
#create an array of indices
col_indices=np.array([0,1,2,0])
row_indices=np.arange(4)
print("Col indices picked: ",col_indices)
print("Row indices picked: ",row_indices)



#Examine the pairings of row_indices and col_indices
for row,col in zip(row_indices,col_indices):
    print(row,col)


print("Values in the array at those indices:\n",ex10[row_indices,col_indices])
ex10[row_indices,col_indices]+=30000
print(ex10)


print("Cesar Sinchiguano")


















#Link to introToNumpy.py
#https://github.com/Sinchiguano/software_engineering_1/blob/main/ai/tuesday292022/introToNumpy.py