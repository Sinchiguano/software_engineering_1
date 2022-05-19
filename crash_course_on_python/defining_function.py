def sayhello():
	'''
	PRINTS HELLO 
	'''
	print('Hello')


sayhello()

def double(value):
	return value*2



def product(value1, value2, value3):
	prod=value1*value2
	prod=prod*value3
	return prod

print(double(2))
print(product(1,2,3))


def fahrenheit_to_celsius(fahrenheit):
	offset=32
	multiplier=5/9
	celsius=(fahrenheit-offset)*multiplier
	print('inside function: ', fahrenheit,offset, multiplier, celsius)

	return celsius

fahrenheit_to_celsius(95) 


import numpy as np
print (numpy._version_)
import math 

x_0, y_0=2,2
x_1, y_1=5,6

print('FIRST POINT IS: ', x_0,y_0)
print('SECOND POINT IS: ',x_1,y_1)


def compute_distance_between_2_points(x_0,y_0,x_1,y_1):
	X=x_1-x_0
	Y=y_1-y_0
	distance=np.square(X)+np.square(Y)
	return math.sqrt(distance)



print(compute_distance_between_2_points(x_0,y_0,x_1,y_1))