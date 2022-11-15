import numpy as np
from abc import ABC, abstractmethod

class Book:
    '''The __init__ special method, also known as a Constructor,
    is used to initialize the Book class with attributes such as title,
    quantity, author, and price.'''
    def __init__(self, title, quantity,author, price):
        self.title=title
        self.quantity=quantity
        self.author=author
        self.__price=price
        self.__discount=None

    def set_discount(self,discount):
        self.__discount=discount
    def get_price(self):
        if self.__discount:
            return self.__price*(1-self.__discount)
        return self.__price
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"

class Novel(Book):
    def __init__(self,title, quantity, author, price, pages):
        super().__init__(title,quantity,author,price)
        self.pages=pages
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}, Pages: {self.pages}"


class Academic(Book):
    def __init__(self,title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price,)
        self.branch=branch
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()},Branch: {self.branch}"




novel1=Novel('Two states',20,'cesar chiriboga',200,187)
novel1.set_discount(0.20)



novel2=Academic('Two states',20,'cesar chiriboga',200,'IT')


print(novel1)
print(novel2)
print(novel1.pages)
print(novel2.branch)



# bulk_book=Book('Python',25,'Cesar Sinchiguano',200)
# bulk_book.set_discount(0.20)


# print(single_book.get_price())
# print(bulk_book.get_price())






















# book1=Book('Book 1',12,'Author 1',120)
# book2=Book('Book 2',18,'Author 2',130)
# book3=Book('Book 3',32,'Author 3',320)



# print(book1)
# print(book1.title)
# print(book1.quantity)
# print(book1.author)
# # print(book1.price)
# # print(book1.__discount)


# single_book=Book('C++',1,'Cesar Sinchiguano',200)

#https://www.freecodecamp.org/news/object-oriented-programming-in-python/

'''In Python, built-in classes are named in lower case, 
but user-defined classes are named in Camel or Snake case,
with the first letter capitalized.'''