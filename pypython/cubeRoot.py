cube=float(input("Enter a number in order to look for the cube root: "))


epsilon=0.01
guess=0.0
increment=0.01
numberGuesses=0


while abs(guess**3 - cube)>=epsilon and guess<=cube:
	guess+=increment
	numberGuesses+=1

print("Number of guesses: ",numberGuesses)

if abs(guess**3 - cube>=epsilon):

	print("Failed on cube roof of: ", cube)
else:
	print(guess, "is close to the cube root of ",cube)



