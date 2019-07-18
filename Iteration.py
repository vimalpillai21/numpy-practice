import numpy as np

# a =  np.arange(0,60,5)
# print(a)
#
# b = a.copy()
# b = b.reshape(3,4)
# print("\nReshaped array is given below :- ")
# print(b)
# print("\nlooped array elements are given below")
# for x in np.nditer(b):
#     print(x, end=" ")
print("\n----------------------------------------------------\n")

# The order of iteration is chosen to match the memory layout of an array,
# without considering a particular ordering. This can be seen by iterating over
# the transpose of the above array.
a = np.arange(0,60,5)
a = a.reshape(3,4)
print(a,end="\n\n")

for x in np.nditer(a):
    print(x, end= " ")
print("\n\n")
b = a.T
print(b)
for x in np.nditer(b):
    print(x, end=" ")
