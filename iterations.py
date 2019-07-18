import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)

# If two arrays are broadcastable, a combined nditer object is able to iterate upon them concurrently.
# Assuming that an array a has dimension 3X4, and there is another array b of dimension 1X4,
# the iterator of following type is used (array b is broadcast to size of a).
print('First array is:')
print(a)
print('\n')

print('Second array is:')
b = np.array([1, 2, 3, 4], dtype = int)
print(b)
print('\n')

print('Modified array is:')
for x,y in np.nditer([a,b]):
   print("%d:%d" % (x,y),end=" ")