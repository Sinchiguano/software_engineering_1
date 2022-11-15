import numpy as np
from abc import ABC, abstractmethod

class Book(ABC):
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
    @abstractmethod    
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