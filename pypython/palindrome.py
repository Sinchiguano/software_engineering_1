#yourData = input("ENTER A STRING: ")



#REVERSE STRING
def palindrome(yourData):
	
	x=""
	for i in yourData:
		#print(i)
		x=i+x
		#print(x)

	return x
	#pass



def main():

	yourData = input("ENTER A STRING: ")

	while(True):

		try:
			#print("sinchiguano")
			if yourData==palindrome(yourData):
				print("IT IS A PALINDROME")
			else:
				print("IT IS NOT A PALINDROME")
			yourData = input("ENTER A STRING: ")

		except Exception as e:
			print(str(e))






if __name__=="__main__":
	main()