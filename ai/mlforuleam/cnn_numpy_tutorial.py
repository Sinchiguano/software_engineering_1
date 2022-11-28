import numpy as np
#mrl
#manifiesto de carga

#ARRAYS
arrayData=np.array([1,2,3,4,5,])
print(type(arrayData))

print(arrayData.shape)
arrayData[4]=45
print(arrayData)

arrayDataRank2=np.array([[1,2,3,4,5],[11,22,33,44,55]])
print(arrayDataRank2.shape)



#FUNCTIONS TO CREATE ARRAY
a=np.zeros((3,3))
print(a)

b=np.ones((3,2))
print(b)

c=np.full((3,3),7)
print(c)

d=np.eye(2)
print(d)

e=np.random.random((4,4))
print(e)



aa=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(aa)

bb=aa[:2,:2]
print(bb)



print(aa[1,2])


tmp=np.array([[7,8,9],[1,2,3],[4,5,6],[10,11,12]])
print(tmp)
indeArray=[0,2,0,1]
print("*")
print(tmp[np.arange(4),indeArray])


tmp[np.arange(4),indeArray]+=10
print(tmp)


#BOOLEAN ARRAY INDEXING
print("#BOOLEAN ARRAY INDEXING")
temp=np.array([[5,6,7,8],[1,2,3,4],[9,10,11,12]])
#temp+=10
print(temp)
boolIndex=(temp>2)
print(boolIndex)

print(temp[boolIndex])
print("++++++")
print(temp[temp>2])



#DATATYPE
print("#DATATYPE")
x=np.array([1,2])
print(x.dtype)



x=np.array([1.0,2.0])
print(x.dtype)

x=np.array([1.0,2.0],dtype=np.int64)
print(x.dtype)


