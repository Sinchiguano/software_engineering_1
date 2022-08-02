an_letters="aefhilmnorsxAEFHILMNORSX"



word=input("I will cheer for you! Enter a word: ")
times=input("Enthusiasm level (1-10): ")
i=0


while i < len(word):
	char=word[i]
	if char in an_letters:
		print("Give me an "+char+"! "+char)
	else:
		print("Give me a "+char+"! "+char)

	i+=1
print ("What does that spell")
print(times)
print(type(times))
for i in range (int(times)):
	print(word, "!!!")
