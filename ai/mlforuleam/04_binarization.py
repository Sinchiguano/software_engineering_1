import numpy as np
from sklearn import preprocessing


inputData=np.random.rand(3,2)


print(inputData)


#BINARIZATION



booleanData=preprocessing.Binarizer(threshold=0.6).transform(inputData)


print(booleanData)
