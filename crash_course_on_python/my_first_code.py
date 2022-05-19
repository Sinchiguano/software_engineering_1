'''


Question 1

In this scenario, two friends are eating dinner at a restaurant. 
The bill comes in the amount of 47.28 dollars. 
The friends decide to split the bill evenly between them, 
after adding 15% tip for the service. Calculate the tip, 
the total amount to pay, and each friend's 
share, then output a message saying "Each person needs to pay: 
" followed by the resulting number.
'''

bill = 47.28 
tip = bill * 47.28 
total = bill + tip
share = total/2 
print("Each person needs to pay: " +str(share))


'''
Question 2

This code is supposed to take two numbers, divide one by another so that the result is equal to 1, 
and display the result on the screen. Unfortunately, there is an error in the code. 
Find the error and fix it, so that the output is correct.
'''


numerator = 10
denominator = 10
result = numerator / denominator
print(result)


'''

Question 4

This code is supposed to display "2 + 2 = 4" on the screen, but there is an error. 
Find the error in the code and fix it, so that the output is correct.
'''

print("2 + 2 = " + str(2 + 2))


'''
Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, 
then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
'''


def get_seconds(hours, minutes, seconds):
  return int(3600*hours + 60*minutes + seconds)

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(45,0,15)
result = amount_a+amount_b
print(result)