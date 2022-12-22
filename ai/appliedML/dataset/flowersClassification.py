print("********************")
# CLASSIFICATION TASK
# VERSICOLOR
# SETOSA
# VIRGINICA

# WIDTH PETAL
# HIGHT PETAL#PETALO

# WIDTH SEPAL
# HIGHT SEPAL#SEPALO


print('******************* PANDAS LIBRARY FOR DATA MANIPULATION *********************************')
import pandas as pd
dataset=pd.read_csv("IRIS.csv")
print(dataset.head(10))
print("/////////////////////")
print(dataset.tail(5))
print("/////////////////////")
print(dataset.info())
print("/////////////////////")
print(dataset.groupby('species').size())
print("/////////////////////")
print(dataset.describe())



print('******************* MATPLOTLIB LIBRARY FOR PLOTTING THE DATASET *********************************')

import matplotlib.pyplot as plt

setosa=dataset[dataset['species']=='Iris-setosa']
virginica=dataset[dataset['species']=='Iris-virginica']
versicolor=dataset[dataset['species']=='Iris-versicolor']
print(setosa.head(5))
print(virginica.head(5))
print(versicolor.head(5))


fig,ax=plt.subplots()
fig.set_size_inches(5,4)

#scatter diagrama de dispersion. relation between two variables 
#sepal_length  sepal_width  petal_length  petal_width
ax.scatter(setosa['petal_length'],setosa['petal_width'],facecolor='blue')
ax.scatter(virginica['petal_length'],virginica['petal_width'],facecolor='green')
ax.scatter(versicolor['petal_length'],versicolor['petal_width'],facecolor='pink')


ax.set_xlabel('petal length [cm]')
ax.set_ylabel('petal width [cm]')
ax.grid()
ax.set_title('IRIS PETALS')
# plt.show()


print('******************* PERFORMING CLASSIFICATION  *********************************')

import sklearn
import numpy as np
print(dataset.head(5))


X=dataset.drop(['species'],axis=1)
print(X.head(5))
#CONVERTING INTO NUMPY ARRAY AND ASSIGNING PETAL LENGTH AND PETAL WIDTH 

X=X.to_numpy()
print(X.shape)
X=X[:,(2,3)]


target=[]
# print(len(dataset['species']))
for i in range(len(dataset['species'])):
    if dataset['species'][i]=='Iris-setosa':
        target.append(0)
    elif dataset['species'][i]=='Iris-versicolor':
        target.append(1)
    else:
        target.append(2)

print('////////////////////////////////////////////////////////////////////////')

print('target')
y=np.array(target)
print(y.shape)
print(type(y))



print('////////////////////////////////////////////////////////////////////////')
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Splitting into train and test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.75)

# print(y_train.shape)
# print(y_train)




model=LogisticRegression()
model.fit(X_train,y_train)


print('--------------------------TEST PREDICTIONS-------------------------')
y_predict=model.predict(X_test)





y_predictions=[]
# print(len(dataset['species']))
for i in range(len(y_predict)):
    if y_predict[i]==0:
        y_predictions.append('Iris-setosa')
    elif  y_predict[i]==1:
        y_predictions.append('Iris-versicolor')
    else:
        y_predictions.append('Iris-virginica')

print('---------------PREDICTIONS-------------')
print(y_predictions[:10])


# y_test=y_test.reshape((len(y_test),1))
# y_predict=y_predict.reshape((len(y_predict),1))

print(y_predict.shape)
print(y_test.shape)

# # yAll=np.stack((y_test,y_predict))

# # print('Y REAL',' - ','Y PREDICTION')
# # for i in range(len(y_test)):
# #     print(y_test[i],'  -  ',y_predict[i])
    


# print('--------------------------------EVALUATIONS---------------------------')


# from sklearn import metrics


# print("Precision, Recall, Confusion matrix, in training\n")

# # Precision Recall scores
# # print(metrics.classification_report(y_test,y_predict, digits=3))

# print("CONFUSION MATRIX IN TESTING DATA")
# print(metrics.confusion_matrix(y_test, y_predict))



