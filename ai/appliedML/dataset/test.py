
import numpy as np 
import pandas as pd

import sklearn
import matplotlib
import time
from tqdm import tqdm


def my_function(food):
  for x in food:
    print(x)



fruits = ["apple", "banana", "cherry"]

'''
Python Progress Bar
'''

def main():
  while(True):
    for i in tqdm(range(10)):
      time.sleep(0.1) 
    my_function(fruits)






if __name__=='__main__':
  main()

