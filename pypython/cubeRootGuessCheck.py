cubeRoot=input("Enter a number to find the perfect cube. ")
tmp=int(cubeRoot)
for guess in range (abs(tmp)+1):
    if guess**3>=abs(tmp):
        break
if guess**3!=abs(tmp):
    print(guess," It is not a perfect cube")
else:
    if guess<0:
        guess=-guess
    print("Cube root of "+str(guess)+" is "+str(guess))
