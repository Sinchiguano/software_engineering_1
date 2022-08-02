x=6
y=3

print(x,y)

def swapFunction(val1,val2):
	tmp=val1
	val1=val2
	val2=tmp
	return val1,val2

print(swapFunction(x,y))
