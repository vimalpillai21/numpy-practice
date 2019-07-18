import numpy as np

a = np.arange(0,60,5)
a = a.reshape(3,4)
# iterating in C and F style
print(a)

print("\nTranspose of a matrix is : -")
b = a.T
print(b, end="\n\n")

print("Sorted in C style")
c = b.copy(order='C')
print(c)

for x in np.nditer(c):
    print(x, end=" ")
print()

print("\nSorted in F style")
c = b.copy(order='F')
print(c)

for x in np.nditer(c):
    print(x, end=" ")

# It is possible to force nditer object to use a specific order by explicitly mentioning it.
print("Forcing nditer to ")
a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print('\n')

print('Sorted in C-style order:')
for x in np.nditer(a, order = 'C'):
   print(x,end= " ")
print('\n')

print('Sorted in F-style order:')
for x in np.nditer(a, order = 'F'):
   print(x, end=" ")
