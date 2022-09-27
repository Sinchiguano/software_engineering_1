import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split




fruits=pd.read_table("fruit_data_with_colors.txt")

print(fruits.head(20))


X=fruits[['mass','width','height','color_score']]
Y=fruits['fruit_label']



x_train, x_test,y_train,y_test=train_test_split(X,Y,random_state=0)
