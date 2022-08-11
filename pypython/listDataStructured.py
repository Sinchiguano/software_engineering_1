listData=[1,2,3,4,5,6]


anotherList=[5,6,8,9]


listData.pop(2)


list1=[1,2,3]
list2=[7,8,9]




listData.extend(anotherList)
for i in listData:
	print(i)



for x,y in zip(list1,list2):
	print(x," ",y)


listData1=[10,20,30]
listData2=listData1
listData3=list(listData1)



listData1[1]=48


print(listData1)
print(listData2)
print(listData3)


#tuples


tuple1=("honda","civic",4,2017)

print(tuple1)

for i in tuple1:
	print(i)



#dictionary





dict1= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(dicttmp))

for key,value in dict1.item():
	print(key)
	print(value)