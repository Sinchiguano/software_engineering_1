age=27

name="Lucy"

if (age<31):
	print("No beer for you")
	#pass

if name is "Cesar":
	print("hey there Cesar")
elif name is "Lucy":
	print("what's up Lucy ")
else:
	print("nothing")



foods=['bacon','tuna','ham','anausages', 'beef']


print(len(foods))
for food in foods:
	print(food)

print("another way to print the stuff")



print("location  ","        item")
for i in range (len(foods)):
	print(foods[i],"    ",i)




for food in foods[:2]:
	print(food)