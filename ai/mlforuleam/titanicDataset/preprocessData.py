"""
https://builtin.com/machine-learning/how-to-preprocess-data-python
"""



import numpy as np
#from pandas import DataFrame, read_csv
import pandas as pd

#LOAD THE DATA IN PYTHON


df=pd.read_csv('train.csv')


# print(df.head(10))
# print("###########################")
# print(df.loc[4])
print("###########################")
print(df.info())


"""
Let's try to drop some of the columns which will not contribute much """

dropColumns=['Name','Ticket','Cabin']
df=df.drop(dropColumns,axis='columns')

print("###########################")
#print(df.info())
#print(df.head(45))


#df=df.dropna()
#print(df.info())

#Creating Dummy Variables


dummies=[]
cols=['Pclass','Sex','Embarked']
for i in cols:
    dummies.append(pd.get_dummies(df[i]))
print(dummies)
titaniDummies=pd.concat(dummies,axis=1  )

df=pd.concat((df,titaniDummies),axis='columns')

#print(df.info())

df=df.drop(['Pclass','Sex','Embarked'],axis='columns')
print(df.info())


#TAKE CARE OF MISSING DATA
df['Age']=df['Age'].interpolate()
print(df.info())

#CONVERT THE DATA FRAME TO NUMPY 

print(df.columns)
print("lllllll")
print(df.index)

x=df.values
y=df['Survived'].values
x=np.delete(x,1,axis=1)

print(x[:2])

#DIVIDE DE DATA SET INTO TRAINING DATA AND TEST DATA
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
