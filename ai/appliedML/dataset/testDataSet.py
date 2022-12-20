print("*****************************************************")

import pandas as pd

#LOADING THE FILES

# data=pd.read_csv('heart.csv')
# data=pd.read_csv('covid.csv')
data=pd.read_csv('diabetes.csv')
# data=pd.read_csv('IRIS.csv')





print("*****************************************************")
print(data.head(10))
print(data.info())
print(data.describe().round())
print(data.keys())



print("*****************************************************")
# import numpy as np
# X=data.drop(['Sex','ChestPainType','RestingBP','RestingECG','ExerciseAngina', 'Oldpeak', 'ST_Slope','HeartDisease'],axis=1)
# y=data['HeartDisease']
# #dataset=data['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak','HeartDisease'] 
# print(X.head(4))




# X=X.to_numpy()
# y=y.to_numpy()
# print(type(X))
# print(type(y))
# print(y[:10])

# # Splitting into train and test
# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=42)

# from sklearn.linear_model import LogisticRegression

# log_reg = LogisticRegression()
# log_reg.fit(X_train,y_train)