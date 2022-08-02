x=3
ans=0
intersLeft=x

while(intersLeft !=0):
    ans=ans+x
    print("ans:",ans)
    intersLeft=intersLeft-1
    print("intersLeft:",intersLeft)
print(str(x)+"*"+str(x)+"="+str(ans))



"""
Input and output

"""

x=1
print(x)
print("my favorite num es"+" "+str(x))

x=5
if x!=5:
    print("I am here")
else:
    print("Not, I am not")
print("we are in a new line ")
n=0
for n in range(5):
    print(n)


tmp=0
for i in range(7,10):
    tmp+=i
print(i)



tmp=0
for i in range(7,20,2):
    tmp+=i
print(i)





tmp=0
for i in range(7,20,2):
    tmp+=i
    if tmp>=10:
        break
print(i)



count=0
for letter in "Snow":
    print(letter)