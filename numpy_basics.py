import numpy as np

# TODO uncomment all these statements
a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [5, 4, 5]])
print(b)

c = np.array([[1, 2], [3, 4, 5]], ndmin=2)
print(f"third array - {c}")

d = np.array([1, 2, 3], dtype=complex)
print(d)

dt = np.dtype(np.int8)
print(dt)

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2','i4', etc.

dt = np.dtype('f8')
print(dt)

dt = np.dtype('>i4')
print(dt)

b = np.array([1, 2, 3], dtype=dt)
b.dtype = 'f2'
print(b)

dt = np.dtype([('age', np.int8)])
print(dt)
arr = np.array([20, 30, 40], dtype=dt)
arr1 = np.array([(20,), (30,), (40,)], dtype=dt)
print(arr)
print(f"array 1 - {arr1}")

# complex numpy data type

student = np.dtype([('name', 'U8'), ('age', 'i1'), ('marks', 'f4')])
print(student)

student1 = np.array([('Person1', 22, 34.45), ('Person2', 24, 45.678)], dtype=student)
print(f"student - {student1}")
print(f"student to list - {student1.tolist()}")

student2 = np.array([[('Student1', 22, 34.45), ('Student2', 24, 45.678)], [('Student3', 22, 34), ('Student4', 45, 34)]],
                    dtype=student)
print(student2)
# print(dir(student1))
