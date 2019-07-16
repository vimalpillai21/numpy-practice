import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print(a)
print(f"Shape of array a - {a.shape}")

for index, item in enumerate(a.shape):
    print(f"Item - {index + 1} = {item}")

a.shape = (3, 2)
print(f"Shape changed a - \n{a}")

b = np.array([[1, 2, 3], [7, 8, 9]])
print(b)
print(f"The shape of b array - {b.shape}")
reshaped_array = b.reshape(3, 2)
print(f"After reshaping reshaped_array - {reshaped_array.shape}")

arange_array = np.arange(0, 100, 5)
print(arange_array)

new_arange_array = np.arange(24)
print(f"new_arange_array size - {new_arange_array.itemsize}")
b = new_arange_array.reshape(2, 3, 4)
print(new_arange_array)
print()
print(f"Reshaped array - \n {b}")
a = [x*2 for x in range(10)]
print(f'value of a after one line - {a}')

fruit = "apple"
isFruit = True if fruit == "apple" else False

print(isFruit)
a = [1, 2, 3]
string = str(input("Enter a string\t"))
# b = "double"
c = [num * 2 for num in a] if string == "double" else ['a', 'b', 'c']
print(c)

array = np.array([1,2,3],dtype="int64")
print(array.itemsize)