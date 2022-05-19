'''
The longest_word function is used to compare 3 words. 
It should return the word with the most number of characters 
(and the first in the list when they have the same length). Fill in the blank to make this happen.
'''


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))