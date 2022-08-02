x="Hello"


print(x)



print(x.lower())

for i in range (0,10):
	print(i)

print("///////////")
for i in range (0,10,2):
	print(i)


print("////////////////")
for i in range (2,12,3):
	print(i)


print("////////////////")
i=2
while i<12:
	print(i)
	i+=1
print("##################")

for i in range(0,10):
	if i ==0:
		continue
	if i%2==0:
		print("The number is even: ",i)
	else:
		print("The number is odd: ",i)

print("###############")
def my_abs(val):
	if val<0:
		print(0-val)
	else:
		print(val)
	

x=my_abs(-2.7)
print(x)