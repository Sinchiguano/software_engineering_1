'''
1.
Question 1

This function converts miles to kilometers (km).

    Complete the function to return the result of the conversion

    Call the function to convert the trip distance from miles to kilometers

    Fill in the blank to print the result of the conversion

    Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result
'''

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2*my_trip_km))


'''
2.
Question 2

This function compares two numbers and returns them in increasing order.

    Fill in the blanks, so the print statement displays the result of the function call in order.

Hint: if a function returns multiple values, don't forget to store these values in multiple variables
'''

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)



def positive_number(number):
	if number>0:
		return "Positive"
	elif number<0:
		return "Negative"
	else:
		return "Zero"


print(positive_number(5))
print(type(positive_number(5)))
