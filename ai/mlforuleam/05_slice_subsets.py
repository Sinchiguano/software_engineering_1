import numpy as np


#RANK 2 ARRAY 
an_array=np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print(an_array)


#USE ARRAY  
a_slice=an_array[:2,1:3]
print(a_slice)




a_slice=an_array[1:3,1:3]
print(a_slice)


print("BEFORE: " , an_array[2,2])
an_array[2,2]=3838
print("AFTER: " , an_array[2,2])

a_slice1=np.array(an_array[:2,1:3])
print(a_slice1)


#USE BOTH INTEGER INDEXING AND SLICE INDEXING

an_array=np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print(an_array)


print("###############")
row_rank1=an_array[1,:]
print(row_rank1)
print(row_rank1.shape)


print("###############")
row_rank1=an_array[1:2,:]
print(row_rank1)
print(row_rank1.shape)



#ARRAY INDEXING FOR CHANGING ELEMENTS
print("###############")
an_array=np.array([[11,12,13,14],[21,22,23,24],[31,32,33,34]])
print("ORIGINAL")
print(an_array)

#create an array of indices
col_indices=np.array([0,1,2,0])
print("\n Col indices picked : "col_indices)
row_indices=np.arange(4)
print("\n Col indices picked : "col_indices)












