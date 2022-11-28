import numpy as np


x=np.array([[1,2,3], 
            [4,5,6]])

v=np.array([1,2,3])
y=np.empty_like(x)


print(y)


for i in range(2):
    y[i,:]=x[i,:]+v

print(y)


print("]]]]]]]]]]]]]")

vv=np.tile(v,(2,1))
print(vv)

y=x+vv
print(x)




x=np.array([[1,2,3], 
            [4,5,6]])


v=np.array([1,2,3])


print(x+v)
w=np.array([4,5])

print(x)
print(x.T)
print(w)
print((x.T+w).T)


print(w)
print(w.shape)
print(w.reshape(2,1))
r=w.reshape(2,1)
print(r.shape)
print(x.shape)
print(r)
print(x)
print(x+r)
print(x*2)
