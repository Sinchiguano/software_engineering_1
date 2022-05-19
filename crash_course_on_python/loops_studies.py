

variable1=0
while(variable1<5):
	print('Not yet the value x='+str(variable1))
	variable1=variable1+1


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

print('another test')
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(str(n))
		n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
