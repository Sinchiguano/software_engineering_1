#ARRAY MATH
print("#ARRAY MATH")
import numpy as np

x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)


#ELEMENT WISE SUM
print(x+y)
print(np.add(x,y))

print("+++++++")
print(x-y)
print(np.subtract(x,y))

print("+++++++")
print(x*y)
print(np.multiply(x,y))

print("+++++++")
print(x/y)
print(np.divide(x,y))

print("+++++++")

print(np.sqrt(x,y))


x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)

v=np.array([9,10],dtype=np.float64)
w=np.array([11,12],dtype=np.float64)


#INNER PRODUCT OF VECTORS
print(v.dot(w))
print(np.dot(v,w))

print(x.dot(y))
print(np.dot(x,y))


x=np.array([[1,2],
            [3,4]])
print(x.sum())
print(np.sum(x))
print(np.sum(x,axis=0))
print("+++")
print(np.sum(x,axis=1))



print("TRANSPOSE")
x=np.array([[1,2],
            [3,4]])


print(x)
print(x.T)

v=np.array([9,10])
print(v.T)