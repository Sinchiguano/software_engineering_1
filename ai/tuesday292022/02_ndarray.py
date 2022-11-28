
import numpy as np


print("*************************")
ex1=np.array(([[1,2,3,4],
                [11,22,33,44],
                [111,222,333,444]]))
print(ex1)

ex1_slice=ex1[:2,:2]
print(ex1_slice)


print("Before:\n ",ex1_slice)
ex1_slice[1,1]=9
print("After:\n ",ex1_slice)


#USE BOTH INTEGER INDEXING AND SLICE INDEXING

b_slice=np.array([[11,12,13],
                    [21,22,23],
                    [31,32,33]])
print(b_slice)
a_row=b_slice[1,:]
print(a_row)
print("*************************")
b_row2=b_slice[1:2,:]
print(b_row2)
print("*************************")
#WE CAN DO THE SAME FOR COLUMNS OF AN ARRAY 
col_rank1=b_slice[:,1]
print(col_rank1)

col_rank2=b_slice[:,1:2]
print(col_rank2)
print(col_rank2.shape)


print("*************************")
#ARRAY INDEXING FOR CHANGING ELEMNETS
tmp_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(tmp_array)
