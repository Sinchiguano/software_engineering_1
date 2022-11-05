# Python 3

# Please use the included copy of 98-0.txt, the text of
# of A Tale of Two Cities, by Charles Dickens

import collections

# open the 98-0.txt input file
input_file=open('98-0.txt', encoding="utf8")
stopword_file=open('stopwords', encoding="utf8")

# number of words to print is 10
num_words = 10

# Part 1: setup the SET of stop words to do this:
# 1. create a set (already done for you)
stopwords=set()

# 2. for each word in the stopword file, add the word to the list.
# Hints: you may wish to read in each line, then use line.split() to get each word
#        when adding each word, you'll want to use word.strip() to remove whitespace
# TODO YOUR CODE HERE



# For debugging, you can print your set here:
# print(stopwords)

# Part 2: Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If the word is already present, increase the count.


# 1. create your data structure here - you'll want to use a dictionary like below:
wordcount={}

# 2. For each word in the input file:
#    a. use .lower() to make lower case and .strip() to remove whitespace
#    b. use .replace(<from>,<to>) to replace each ".", ",", "\"" <-- the \" allows
#       you to remove a quotation mark.  For example:
#word="banana".replace("a","0")
#print(word)
#    c. check to make sure the word isn't in the list of stopwords.  If it isn't:
#    d. if the word isn't already in your dictionary, add it with the count of 1.
#       if the word is in the dictionary, add 1 to the present count
# TODO YOUR CODE HERE











# Part 3, we want to print the top n most frequent words
# An easy way to sort your dictionary is to use collections.Counter.
# If you want, collections.Counter may be useful.  For example:
d = collections.Counter(wordcount)

# Lastly, you'll want to iterate through the 10 most common elements
# in the collection, e.g., using d.most_common(10) which returns a tuple
# and print the word and its count
# TODO YOUR CODE HERE
