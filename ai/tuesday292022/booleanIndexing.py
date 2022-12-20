
import numpy as np

#create a 3x2 array
ex1=np.array([[11,12],[21,22],[31,32]])
print(ex1)

#create a filter which will be boolean values for whether each element meets this condition
filter=(ex1>15)
print(filter)

selectedElement=ex1[filter]
print(selectedElement)


print("+++++++++++++++++++++")
#for short, we could just have used the approach below without the need for the separate filter array
print(ex1[ex1>15])


print("+++++++++++++++++++++")

evenValues=ex1[ex1%2==0]
print(f"Even values: {evenValues}")
evenValues+=100
print("+++++++++++++++++++++")
print(f"After adding 100 {evenValues}")



#DATATYPE AND ARRAY OPERATIONS

ex1=np.array([[11,12],[21,22],[31,32]])
print(ex1)
print(type(ex1))
print(ex1.dtype)

ex1=np.array([[11.0,12.0],[21.0,22.0],[31.0,32.0]])
print(ex1)
print(type(ex1))
print(ex1.dtype)



ex1=np.array([[11,12],[21,22],[31,32]],dtype=np.float)
print(ex1)
print(type(ex1))
print(ex1.dtype)


# WE CAN USE THIS TO FORCE FLOATS INTO INTEGERS (USING FLOOR FUNCTION)

ex1=np.array([[11.1,12.1],[21.1,22.1],[31.1,32.1]],dtype=np.int64)
print(ex1)
print(type(ex1))
print(ex1.dtype)

print("+++++++++++++++++++++")
#ARITHMETIC ARRAY OPERATIONS
x=np.array([[4,112],[121,122]],dtype=np.int)
y=np.array([[211.1,212.1],[221.1,222.1]],dtype=np.float64)
print(x)
print()
print(y)
print("+++++++++++++++++++++")
#add
print("ADD")
print(x+y)
totalValue=np.add(x,y)
print(f"The total value is:\n{totalValue}")
print(np.add(x,y))
print("+++++++++++++++++++++")
#SUBTRACT
print("SUBTRACT")
print(x-y)
totalValue=np.add(x,y)
print(f"The total value is:\n{totalValue}")
print(np.subtract(x,y))



#MULTIPLY
print("MULTIPLY")
print(x/y)
totalValue=np.multiply(x,y)
print(f"The total value is:\n{totalValue}")

#DIVIDE
print("SUBTRACT")
print(x-y)
totalValue=np.divide(x,y)
print(f"The total value is:\n{totalValue}")



#SQUARE ROOT
print("SUBTRACT")
print(x-y)
totalValue=np.sqrt(x)
print(f"The total value is:\n{totalValue}")

