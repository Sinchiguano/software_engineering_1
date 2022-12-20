print("Hello world")
tmp1=5
tmp2=10
print(tmp1+tmp2)
print(tmp1-tmp2)
print(tmp1*tmp2)
print(tmp1/tmp2)

valor=8.0
print(type(valor))

'''
HOLA COMO ESTAS
'''
tmp=True
var=False
#CESAR SINCHIGUANO
#HOLA COMO ESTA
print(tmp)
print(tmp and var)
print(tmp or var)
print(not tmp)
s="cesar sinchiguano"
print(s.capitalize())
print(s.upper())

print("*****************")
#CONTAINERS
listVar=[1,2,3,4,5]
print(listVar)
print(listVar[1])
listString=['cesar',2,'juan',]
print(listString[0].upper())
listString[2]="Pepe"
print(listString)
listString.append('julio')
print(listString)


print("*****************")
animals=['cat','dog','monkey']
for i in animals:
    print("Type of animal: ",i)

print("*****************")
numeros=[0,1,2,3,4]
print(numeros)
cuadrados=[]
for i in numeros:
    cuadrados.append(i**2)
print(cuadrados)


print(cuadrados.pop())
print(cuadrados)
print("*****************")
numeros=[0,1,2,3,4]
newSquares=[x**2 for x in numeros]
print(newSquares)


#DICTIONARIES
#dict={'key':'value'}
dict={'cat':'cute','dog':'great'}
print(dict['cat'])
print(dict['cat'])
###

def singFunction(x):
    if x>0:
        return 'POSITIVE'
    elif x<0:
        return 'NEGATIVE'
    else:
        return 'ZERO'
        
listSing=[-1,0,1]
for i in listSing:
    print(singFunction(i))














