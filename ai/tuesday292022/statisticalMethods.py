import numpy as np



#BASIC STATISTICAL OPERATIONS
#setup a random 2x4 matrix
randomArray=np.random.randn(2,4)
print(randomArray)


#COMPUTE THE MEAN FOR ALL ELEMENTS
meanValue=randomArray.mean()
print(f"Mean value: {meanValue}")

#COMPUTE THE MEAN BY ROW
rowMean=randomArray.mean(axis=1)
print(rowMean)

#COMPUTE THE MEAN BY COLUMN
columnMean=randomArray.mean(axis=0)
print(columnMean)

#SUM ALL THE ELEMENTS
sumValue=randomArray.sum()
print(sumValue)

#COMPUTE THE MEDIANS
#the median value from a ordered list
medianValues=np.median(randomArray,axis=1)
print(medianValues)
list=[1,2,3,4,5,6,7]
print(np.median(list))



print("8888888888888888888888")
#SORTING 
#create a 10 elements array of randoms value
unsortedArray=np.random.randn(6)
print(unsortedArray)
sorted=np.array(unsortedArray)
sorted.sort()
print(f"The sorted array is:\n{sorted}")

unsortedArray.sort()
print(unsortedArray)


print("/////////////////////////////")
#FINDING UNIQUE ELEMENTS
someArray=np.array([1,2,2,3,1,5,3,4,2])
print(np.unique(someArray))


#OPERATIONS WITH np.array data type
stringArray1=np.array(['desk','chair','bulb'])
stringArray2=np.array(['lamp','bulb','chair'])
print(stringArray1)
print(stringArray2)
#Return the unique, sorted array of values that are in either of the two input arrays.
tmpString=np.union1d(stringArray1,stringArray2)
print(tmpString)

#elements in s1 that are not in s2
tmpDiff=np.setdiff1d(stringArray1,stringArray2)
print(tmpDiff)

#which element of s1 is also in s2
tmp=np.in1d(stringArray1,stringArray2)


#BROADCASTING
