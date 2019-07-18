import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)

print(a)

# external loop
print("modified array is :-")
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=" ")