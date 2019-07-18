import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a)
#The nditer object has another optional parameter called op_flags.
# Its default value is read-only, but can be set to read-write or write-only mode.
# This will enable modifying array elements using this iterator.
for x in np.nditer(a,op_flags=['readwrite']):
    x[...] = 2*x
print("\n Modified array is :-")
print(a)