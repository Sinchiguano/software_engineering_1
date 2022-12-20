from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris() #Loading the dataset
print(iris.keys())

print(iris["data"])
print(iris["data"].shape)

print(iris["data"][:10])
print(iris["target"][:10])
print(iris["target"])


iris = pd.DataFrame(
    data= np.c_[iris['data'], iris['target']],columns= iris['feature_names'] + ['target'])

print(iris.head(10))
print("#####################")
print(iris)