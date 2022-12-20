import numpy as np


#CREATE ARRAY OF ZEROS
someArray=np.zeros((4,3))
print(someArray)





#CREATE A RANK 1 NDARRAY WITH 3 VALUES
addRows=np.array([1,0,3])
print(addRows)



#ADD TO EACH ROW OF SOMEARRAY ADDROWS
y=someArray+addRows
print(y)


#CREATE AN NDARRAY WHICH IS 4X1 TO BRAODCAST ACROSS COLUMNS
add_cols=np.array([[0,1,2,3]])
print(add_cols)
print(add_cols.shape)
cols_transpose=add_cols.T
print(cols_transpose.shape)
print(someArray+cols_transpose)



#ADD TO EACH COLUMN OF START USING BROADCASTING
someScalar=np.array([1])
print(someScalar)
print(someScalar.shape)
print(someArray+someScalar)


#READ OR WRITE TO DISK 
x=np.array([23.23,24.24])
np.save("x",x)

loadFile=np.load('x.npy')
print(loadFile)


#ADDITIONAL COMMON NDARRAY OPERATIONS
#dot product on matrices and inner product on vectors
a1=np.array([[1,1],[1,1]])
b1=np.array([[2,2],[2,2]])
print(a1.dot(b1))
print(np.dot(a1,b1))
#dot product in vectors of two vectors
vector1=np.array([2,2])
vector2=np.array([1,1])
print("*********************")
print(np.dot(vector1,vector2))


#SUM
#sum elements in array
example1=np.array([[11,22],[21,22]])
print(np.sum(example1,axis=0))#columnwise sum
print(np.sum(example1,axis=1))#rowwise sum




#RESHAPING ARRAY
someArray=np.arange(20)
print(someArray)
print(someArray.shape)
tmpSomeArray=someArray.reshape(4,5)
print(tmpSomeArray)

print("*********************")
#TRANSPOSE
print(tmpSomeArray)
print(tmpSomeArray.T)

print("*********************")
#INDEXING USING WHERE()
someArrayA=np.array([1,2,3,4,5])
someArrayB=np.array([11,22,33,44,55])

someFilter=np.array([True,False,True,False,True])
out=np.where(someFilter,someArrayA,someArrayB)
print(out)



#ANY OR ALL CONDITIONALS
boolArray=np.array([True,False,True,True,False])
print(boolArray.any())
#it will returns true if only if all the items are true otherwise it is going to return false

print(boolArray.all())

#RANDOM NUMBER GENERATION 
tmpRandomNumber=np.random.normal(size=(2,4))
print("*********************")
print(tmpRandomNumber)
print("*********************")


z=np.random.randint(low=6,high=10,size=4)
print(z)


z=np.random.randint(6,10,size=4)
print(z)

print("*********************")
#MERGING DATA SETS

z1=np.random.randint(5,15,size=(2,2))
z2=np.random.randint(5,15,size=(2,2))
print(z1)
print(z2)
print("*********************")
tmpv=np.vstack((z1,z2))
tmph=np.hstack((z1,z2))

print(tmpv)
print(tmph)

print("*********************")
con1=np.concatenate([z1,z2],axis=0)
print(con1)


print("*********************")
con1=np.concatenate([z1,z2.T],axis=1)
print(con1)





















