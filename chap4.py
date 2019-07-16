import numpy as np

x = np.array([[1,2],[3,4],[5,6]])
y = x[[0,1,2],[0,1,0]]
print(x,end='\n')
print(y)

print("----------------------------")

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

print('Our array is:',x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
# the array element coordinates are (0.0), (0,2), (3,0), (3,2)
print('The corner elements of this array are:',y)

print("------------------------------")
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

print('Our array is:',x)

# slicing
z = x[1:4,1:3]

print('After slicing, our array becomes:',z)

# using advanced index for column
y = x[1:4,[1,2]]

print('Slicing using advanced index for column: ',y)

print("---------Boolean Array indexing---------")

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])

print('Our array is:',x)

# Now we will print the items greater than 5
print('The items greater than 5 are:',x[x > 5])

# filtering non nan variables
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print('nan array - ',a)
print(a[~np.isnan(a)])

# filtering complex variables
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])