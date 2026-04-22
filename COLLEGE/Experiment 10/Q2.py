# Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 
import numpy as np

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

sum_of_rows=np.sum(arr,axis=1)
sum_of_columns=np.sum(arr,axis=0)
print("Sum of rows:",sum_of_rows)       
print("Sum of columns:",sum_of_columns)
second_max=np.sort(arr.flatten())[-2]
print("Second maximum element in the array:",second_max)
