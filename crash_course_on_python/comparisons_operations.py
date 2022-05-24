print(7>3)
print(3!=8)
print(3==3)


def greet(friend,money):
	if friend and (money>20):
		money=money-20
		print('hi')
	elif friend:
		print('hello')
	else:
		print('ha ha ha')
		money=money+10

	return money


money=15
money=greet(False, money)
print('MONEY: '+str(money))


import numpy


