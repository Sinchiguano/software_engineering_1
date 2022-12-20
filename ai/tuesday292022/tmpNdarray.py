import numpy as np


tmp=np.array([[1,2,3],[11,22,33]],dtype=float)
print("tmp\n{}".format(tmp))

tmp=np.array([[1.2,2.3,3.0],[11.0,22.0,33.0]],dtype=float)
print("tmp\n{}".format(tmp))

tmp=np.array([[1.2,2.3,3.0],[11.0,22.0,33.0]],dtype=int)
print("tmp\n{}".format(tmp))


tmp=np.random.randn(2,5)
print(tmp.shape)


print(tmp.mean())
print(tmp.mean(axis=0))


tmp=np.random.randn(5)
print("Unsorted array:\n",tmp)
sorted=np.array(tmp)
sorted.sort()
print("Sorted array:\n",sorted)


tmp=np.array([1,2,3,4,5,1,2,3,45,1,2,3,42,3,5,5])
print(np.unique(tmp))

#NUMPY BROADCASTING

a=np.array([1,2,3,4])
b=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a+b)



