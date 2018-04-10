#Slicing

nums = range(5) # range is a built-in function that creates a list of integers
print nums      #prints "[0,1,2,3,4]"
print nums[2:4] #prints "[2,3]"
print nums[2:]  #pirnts "[2,3,4]"
print nums[:2]  #prints "[0,1]"
print nums[:]   #prints "[0,1,2,3,4]"
print nums[:-1] #prints "[0,1,2,3]"
nums[2:4] = [8,9] #Assign a new sublist to a slice
print nums      #prints "[0,1,8,9,4]"

#Indexing, Slicing, Iterating

import numpy as np

a = np.array([1,2,3,4,5])
# array([1, 2, 3, 4, 5])

a[1:3]
# array([2, 3])

a[-1]
# 5

a[0:2] = 9

a   #array([9, 9, 3, 4, 5])

#################################

b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# array([ 1, 2, 3, 4],
#       [ 5, 6, 7, 8],
#       [ 9, 10, 11, 12]])

b[:, 1]
# array ([ 2, 6, 10])

b[-1]
# array([9, 10, 11, 12])

b[-1, :]
# array([9,10,11,12])

b[0:2, :]
#array ([[1,2,3,4],
#       [5,6,7,8]])
