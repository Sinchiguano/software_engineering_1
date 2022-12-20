

print("####")
import pandas as pd
#extra help with pandas methods
#https://www.analyticsvidhya.com/blog/2021/05/pandas-functions-13-most-important/
fruits=pd.read_table("fruit_data_with_colors.txt")
print(type(fruits))
# print(fruits.head(10))
# print(fruits.describe())
#print(fruits.value_counts())


print("////////////////////////////////////")
print(fruits.head(5))
#print(fruits)


from sklearn.model_selection import train_test_split
X=fruits[['height','width','mass','color_score']]
y=fruits[['fruit_label']]

X_Training,X_Testing, y_Training,y_Testing=train_test_split(X,y,random_state=0)


#CREATE THE MODEL
from sklearn.neighbors import KNeighborsClassifier
knn_Model=KNeighborsClassifier(n_neighbors=5)


#FIT THE MODEL WITH THE TRAINING DATASET
knn_Model.fit(X_Training,y_Training)

print('++++++++++++++++++++++++++++++++')
#EVALUATE THE MODEL 
#accuracy=exactitud y precisión
print("Accuracy of the model K-NN classifier on testing set",knn_Model.score(X_Testing,y_Testing))


#CREATE SOME EXAMPLES
realLife=[[5.5,2.2,10,0.70]]# 1 sample, 1 example or 1 instance

print('Predicted fruit type for ',realLife, ' is ', knn_Model.predict(realLife))

