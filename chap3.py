import numpy as np

# x = np.array([1, 2, 3, 4, 5], dtype=np.float64)
# print(x.itemsize)
# print(x.flags)
#
# empty_array = np.empty((2, 3), dtype=np.int32, order='C')
# print(empty_array)
#
# zero_array = np.zeros((3), dtype=np.int, order='C')
# print(zero_array)
#
# x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
# print(x)
#
# y = np.ones((2, 2), dtype=np.int)
# print(y)
# new_y = np.ones([2, 3])
# print(new_y)
#
# z = np.asarray([1, 2, 3], dtype=np.int, order='C')
# print(z)
#
# list_of_tuple = [[(1, 2, 4), (8, 7), (5, 6)], [(5, 6)]]
# new_array = np.asarray(list_of_tuple)
# print(new_array)
# print(new_array.shape)
#
# s = 'Hello World'
# a = np.frombuffer(s, dtype='S1')
# print(a)
#
# list = [1,2,4]
# it = iter(list)
# x =np.fromiter(list, dtype=np.float)
# print(x)

y = np.arange(3,16,3,dtype=np.float32)
print('new array - ',y)

qw = np.linspace(1, 10, 6, endpoint=True, retstep=False, dtype=float)
print(qw)

a = np.arange(10)
print(a)
print(a[2:5])

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)

print('using slicing')
print(a[1:])

print('Our array is:')
print(a)

# this returns array of items in the second column
print('The items in the second column are:')
print(a[..., 1])

# Now we will slice all items from the second row
print('The items in the second row are:')
print(a[1, ...])

# Now we will slice all items from column 1 onwards
print('The items column 1 onwards are:')
print(a[..., 1:])

a = 2
assert a==1,'error'
print('hello world')