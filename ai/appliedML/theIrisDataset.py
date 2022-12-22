
print('***************************************')

from sklearn import datasets

#WORKING WITH NUMPY ARRAY AS DATA STRUCTURE
#https://www.geeksforgeeks.org/numpy-ndarray/
dataSet=datasets.load_iris()
##############################################################
print('////////////////////////////////  DATA   ///////////////')
print(type(dataSet))
print(dataSet.keys())
print(dataSet['data'].shape)
print(type(dataSet['data']))
print(dataSet['data'][:10,:])
data=dataSet['data']
print('**************************************************')
print('/////////////////////////////  TARGET   ////////////////')
import numpy as np
print(type(dataSet['target']))
print('target shape: {}'.format(dataSet['target'].shape))
target=np.reshape(dataSet['target'],(150,1))
print('target shape: {}'.format(target.shape))
print(target[:10,:])


#arr = np.array([4, 7, 12])
print('**************************************************')
print('/////////////////////////////  FEATURES NAMES  ////////////////')
print(dataSet['feature_names'][:])
print(type(dataSet['feature_names']))
print('Coverting to numpy array')
feature_names=np.array(dataSet['feature_names'])
print('Feature names shape: {}'.format(feature_names.shape))
features=np.reshape(feature_names,(1,4))
print('Feature names shape: {}'.format(features.shape))
print('**************************************************')



print('**************************************************')
print('/////////////////////////////  USING PANDAS  ////////////////')
#CONVERTING THE DATASET TO PANDAS DATAFRAME
import pandas as pd
targetNew=np.array(['target'])
print(targetNew.shape)
newTarget=np.reshape(targetNew,(1,1))
print(newTarget.shape)
tmpConcatenation=np.concatenate((features,targetNew),axis=None)
print(tmpConcatenation.shape)



iris=pd.DataFrame(
        data=np.hstack((data,target)),
        columns=tmpConcatenation)

print(type(iris))
print(iris.head(5))

species=[]
print('len of target: {}'.format(len(iris['target'])))
counter=len(iris['target'])
for i in range(counter):
    if iris['target'][i]==0:
        species.append('setosa')
    elif iris['target'][i]==1:
        species.append('versicolor')
    else:
        species.append('virginica')

iris['species']=species
print(iris.head(5))


print('**************************************************')
print('///////////////////////////// STATISTICAL INFORMATIONS ////////////////')
print('DESCRIBE')
print(iris.describe())


print('**************************************************')
print('///////////////////////////// PLOTTING THE DATASET ////////////////')

import matplotlib.pyplot as plt

#we can use both statement or expression in writing or speech
# print(iris.species=='setosa')
# print('-----')
# print(iris['species']=='setosa')

setosa = iris[iris['species']=='setosa']
versicolor = iris[iris['species']=='versicolor']
virginica = iris[iris['species']=='virginica']

# setosa = iris[iris.species=='setosa']
# versicolor = iris[iris.species=='versicolor']
# virginica = iris[iris.species=='virginica']


# print(setosa.head(5))
# print(versicolor.head(5))
# print(virginica.head(5))


fig, ax=plt.subplots()
fig.set_size_inches(13,7)#adjusting the length and width of the plot
# ax.scatter(setosa['sepal length (cm)'],setosa['sepal width (cm)'])
# ax.scatter(versicolor['sepal length (cm)'],versicolor['sepal width (cm)'])
# ax.scatter(virginica['sepal length (cm)'],virginica['sepal width (cm)'])

# ax.scatter(setosa['sepal length (cm)'],setosa['sepal width (cm)'],label='Setosa',facecolor='blue')
# ax.scatter(versicolor['sepal length (cm)'],versicolor['sepal width (cm)'],label='Versicolor',facecolor='green')
# ax.scatter(virginica['sepal length (cm)'],virginica['sepal width (cm)'],label='Virginica',facecolor='red')


ax.scatter(setosa['petal length (cm)'], setosa['petal width (cm)'], label="Setosa", facecolor="blue")
ax.scatter(versicolor['petal length (cm)'], versicolor['petal width (cm)'], label="Versicolor", facecolor="green")
ax.scatter(virginica['petal length (cm)'], virginica['petal width (cm)'], label="Virginica", facecolor="red")


ax.set_xlabel('petal length [cm]')
ax.set_ylabel('petal width [cm]')
ax.set_title('Iris petals')
ax.legend()
ax.grid()
# plt.show()
   

print('**************************************************')
print('///////////////////////////// PERFORMING CLASSIFICATION  ////////////////')
#BEFORE IMPORTING OUR LOGISTIC MODEL WE NEED TO CONVERT OUR PANDAS DATA FRAME INTO NUMPY ARRAY
#dropping the target and species 

# X=iris.drop(['target','species'],axis=1)
# XX=iris.drop(['target','species'],axis=1)
# print(X.shape)
# print(type(X))
# # print(X.head(10))
# # print(iris['target'].head(5))
# # print(X[:,:])
# X=X.to_numpy()
# print(type(X))
# print(X.shape)
# print(X[:6,:])
# print('----------------------------------------------------------')
# XX=XX.to_numpy()[:,2:]
# # XX=XX.to_numpy()[:,(2,3)]
# print(type(XX))
# print(XX.shape)
# print(XX[:6,:])


X=iris.drop(['target','species'],axis=1)
X=X.to_numpy()[:,2:]#take all the row and column 2 and 3
y=iris['target']
print('TARGET')
print(y.shape)
print(type(y))

print('////////////////////////////////')

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=42)

print(y_train.shape)
print(y_train)

# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()
# model.fit(X_train,y_train)




# print('Training predictions')
# predicTraining=model.predict(X_train)
# print(predicTraining)

# print('Testing predictions')
# predicTesting=model.predict(X_test)
# print(predicTesting)

# print('**************************************************')
# #FOR CLASSIFICATION PROBLEMS THREE MEAIN MEASUREMENTS
# #PRECISION
# #RECALL
# #CONFUSION MATRIX

# # from sklearn import metrics
# # print(metrics.classification_report(y_train,predicTraining,digits=3))
# # print('Confusion matrix')
# # print(metrics.confusion_matrix(y_train,predicTraining))


# # print('**************************************************')
# # from sklearn import metrics
# # print(metrics.classification_report(y_test,predicTesting,digits=3))
# # print('Confusion matrix')
# # print(metrics.confusion_matrix(y_test,predicTesting))



# # #https://www.pycodemates.com/2022/05/iris-dataset-classification-with-python.html

