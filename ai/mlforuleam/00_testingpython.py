
import numpy as np
from sklearn import preprocessing



#SAMPLE DATA
print("#SAMPLE DATA")
inputData=np.random.rand(3,4)
print(inputData)




#PREPROCESSING SCALE
print("#PREPROCESSING SCALE")
inputScale=preprocessing.scale(inputData)
print(inputScale)



#STANDARD DEVIATION
print("#STANDARD DEVIATION")
inputDeviation=inputData.std(axis=0)
print(inputDeviation)



#AFTER SCALING
print("#AFTER SCALING")
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,10))
dataScaled=data_scaler.fit_transform(inputData)
print(dataScaled)