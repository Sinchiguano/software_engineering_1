import numpy as np

#GETTING STARTED WITH NUMPY 
#CREATE ARRAY OF RANK 1
aArray=np. array([[3,33,333],
                  [1,11,111]])
print(aArray)
print(aArray.shape)
print(aArray[1,1])
aArray[1,1]=88
print(aArray)

bArray=np.random.rand(3,2)
print(bArray)
print(f"The shape is 2 rows, 3 columns: {bArray.shape}")

#THERE ARE MANY WAYS TO CREATE NUMPY ARRAYS
ex1=np.zeros((4,3))
print(ex1)

ex2=np.full((3,3),8)
print(ex2)


ex3=np.eye(3,3)
print(ex3)


ex4=np.random.random((3,2))

print("///////////////////////////////")
#ARRAY INDEXING
ex5=np.random.random((4,4))
print(ex5)
subArray=ex5[1:3,1:3]
print(subArray)


subArray=np.array([ex5[:,0]])
print(subArray.shape)

subArray+=100
print(subArray)




print("///////////////////////////////")
#USE BOTH INTEGER INDEXING AND SLICE INDEXING
ex6=np.random.random((4,4))
print(ex6)
row_sample1=ex6[0,:]
print(f"The first row and all the columns")
print(row_sample1)

#CREATE ARRAY OF INDICES
col_indices=([0,1,2,0])
row_indices=(np.arange(4))

print("Columns indices picked: \n",col_indices)
print("Row indices picked: \n",row_indices)
for row, columns in zip(row_indices,col_indices):
    print(row,",",columns)
print("CESAR SINCHIGUANO")
print(ex6[row_indices,col_indices])
#BOOLEAN INDEXING
ex7=np.random.random((3,2))
print(ex7)
filterArray=(ex7<0.5)
print(filterArray)
newArray=ex7[filterArray]
print(newArray)

#ARITHMETIC ARRAY OPERATIONS
x=np.array([[1,2],[3,4]])
y=np.array([[3,4],[5,6]])
print(x)
print()
print(y)
print("------------")

print(x-y)
print(x+y)
print(x*y)
print("------------")
print(np.sqrt(x))
print(np.sqrt(y))


print("*******************")
#Statistical Operations
tmpArray=10*np.random.randn(2,3)
print(tmpArray)
print(tmpArray.mean())
#COMPUTE THE MEAN BY ROW
print(tmpArray.mean(axis=1))
#COMPUTE THE MEAN BY COLUMN
print(tmpArray.mean(axis=0))
print("The sum of all the elements: {}".format(tmpArray.sum()))


#SORTING NUMBER
print("Sorting list ")
unsorterList=np.random.randn(6)
print("Unsorted list: \n{}".format(unsorterList))
sortedList=np.array(unsorterList)
sortedList.sort()
print("Sorted list: \n{}".format(sortedList))

list=np.array([1,2,1,2,3,5,2,3,5,3,5,9])
uniqueElements=np.unique(list)
print("The elements of the list: {}".format(list))
print("The unique elements of the list: {}".format(uniqueElements))


#BROADCASTING
print("#BROADCASTING")
import numpy as np
start=np.zeros((3,3))
print(start)
row=np.array([[1],[2],[3]])
print(row.shape)
y=start+row
print(y)

col=np.array([[11,22,33]])
print(col.shape)
print(start+col)

#ADD A SCALAR
addScalar=np.array([[1]])
print(addScalar.shape)
print(start+addScalar)







