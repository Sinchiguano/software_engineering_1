


counter=0

def quicksort(unsortList):
    global counter
    if len(unsortList)<=1:
        return unsortList
    pivot=unsortList[len(unsortList)//2]
    # print(pivot)
    left=[x for x in unsortList if x<pivot]
    middle=[x for x in unsortList if x==pivot]
    right=[x for x in unsortList if x > pivot]
    # print(left)
    # print(middle)
    # print(right)
    # print(f'Counter: {counter}')
    counter = counter+1
    return quicksort(left)+middle+quicksort(right)

unsortList=[3,6,8,10,1,2,1]
print(quicksort(unsortList))


#BASIC DATA TYPE
#NUMBERS
x=3
tmp=5
print(tmp)
print(type(tmp))
print(x+1)
print(x-1)
print(x*2)
print(x**2)
x=5
x+=1
x*=1
x=2.5
print(type(x))


#BOOLEANS (&&,||,etc)
tmp1=True
tmp2=False
print(tmp1, tmp2)
print(type(tmp1))
print(tmp1 and tmp2)
print(tmp1 or tmp2)
print(not tmp2)
print(tmp2!=tmp1)


#STRINGS


myName="cesar Sinchiguano"
greetingVariable="Hello"

print(f"{greetingVariable}, {myName}")
print(greetingVariable+', '+myName)
print("%s %i %s"%("Hello, ",12, "  Sinchiguano"))
#STRING OBJECT HAS A BUNCH OF USEFUL METHODS; FOR EXAMPLE
print(myName.capitalize())
print(myName.upper())
print(myName.replace('S', 'C'))



#CONTAINERS

myList=[3,2,5]
print(myList,myList[2])

myList[2]="Cesar Sinchiguano"
print(myList,myList[2])




myList.append("Chiriboga")
print(myList)
print(myList.pop())
print(myList)

myNumbers=list(range(15))
print(myNumbers)
print(myNumbers[2:6])
print(myNumbers[2:])
print(myNumbers[:6])
print(myNumbers[2:-1])#the last one nope
myNumbers[:6]=myNumbers[8:]
print(myNumbers)


#LOOPS 

myAnimals=["cow","girafe","monkey"]
for eachAnimal in myAnimals:#
    print(eachAnimal)

myAnimals=["cow","giraffe","monkey"]
for element,eachAnimal in enumerate(myAnimals):
    print(f"Item: {element+1} and Animal: {eachAnimal}")


#LIST COMPREHENSIONS
someNumbers=list(range(5))
squareNumbers=[]
print(someNumbers)
for eachNumber in someNumbers:
    squareNumbers.append(eachNumber**2)
print(squareNumbers)



#  THIS IS A BETTER WAY TO DO WITH LIST COMPREHENSIONS
someNumbers=list(range(5))
squareNumbers=[x**2 for x in someNumbers]
print(someNumbers)
print(squareNumbers)

print("THIS IS A BETTER WAY TO DO WITH LIST COMPREHENSIONS")
#  THIS IS A BETTER WAY TO DO WITH LIST COMPREHENSIONS
someNumbers=list(range(5))
evenSquareNumbers=[x**2 for x in someNumbers if x%2==0]
print(someNumbers)
print(evenSquareNumbers)


#DICTIONARIES
print("DICTIONARIES")


myDictionary={
    'cat':'cute',
    'dog':'furry'}
print(myDictionary['cat'])
print('cat' in myDictionary)
myDictionary['fish']='wet'
for key,value in myDictionary.items():
    print(f"{key} --> {value}")

for key in myDictionary.keys():#
    print(f"{key} ")

for value in myDictionary.values():
    print(f"{value} ")



del myDictionary['fish']
for key,value in myDictionary.items():
    print(f"{key} --> {value}")

print(myDictionary.get('monkey','N/A'))
for key,value in myDictionary.items():
    print(f"{key} --> {value}")


#ANOTHER WAY TO PRINT INFORMATION FROM A DICTIONARY
print("ANOTHER WAY TO PRINT INFORMATION FROM A DICTIONARY")
for tmp in myDictionary:
    print(tmp, '-->',myDictionary[tmp])


#DICTIONARY COMPREHENSION 

enumerateDictionary=list(range(5))
evenNumerateSquare={x:x**2 for x in enumerateDictionary if x%2==0}

for key in evenNumerateSquare :
    print(key, '-->',evenNumerateSquare[key])




#SET
animalSet={"cat","dog"}
print(animalSet)
print("cat" in animalSet)
animalSet.add('fish')
print("fish" in animalSet)

print(len(animalSet))
animalSet.remove('cat')
print(len(animalSet))


for n,classAnimal in enumerate(animalSet):
    print(f"%i: %s"%(n,classAnimal))



#SET COMPREHENSION 
from math import sqrt
print("#SET COMPREHENSION ")
animalSetSquare={x for x in range(30)}
print(animalSetSquare)

animalSetSquare={sqrt(x) for x in range(30)}
print(animalSetSquare)

animalSetSquare={int(sqrt(x)) for x in range(30)}
print(animalSetSquare)


#TUPLES

print("#TUPLES")
newDictionary={(x,x+1):x for x in range(10)}
for tmp in newDictionary:
    print(tmp, '-->',newDictionary[tmp])

newTuple=(5,6)
print(type(newTuple))
print(newDictionary[newTuple])
print(newDictionary[(1,2)])


#FUNCTIONS
print("#FUNCTIONS")


def sign(tmp):
    if tmp<0:
        return "NEGATIVE"
    elif tmp==0:
        return "ZERO"
    elif tmp>0:
        return "POSITIVE"




for x in [-1,0,+1]:
    print(sign(x))



def hello(name,flag=False):
    if flag:
        print(f"Hello, {name.upper()}")
    else:
        print(f"Hello, {name}")
    
hello("Cesar")
hello("Cesar Sinchiguano", True)



print("#CLASSES")

#CLASSES
class greeting():
    #constructor
    def __init__(self, name):
        self.name=name
    #Instance method
    def greet(self, flag=False):
        if flag:
            print(f"HELLO, {self.name.upper()}")
        else:
            print(f"Hello, {self.name}")



name1=greeting("Cesar Sinchiguano")
name1.greet()
name1.greet(False)
name1.greet(True)
name1.greet(flag=True)