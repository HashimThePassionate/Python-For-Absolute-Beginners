import ctypes
import sys
a = [1, 2, 3]
print(f'Address of A = {id(a)}')
# print(f'Reference of A = {sys.getrefcount(a)}')

# b = a
# print(f'Address of A = {id(a)}')
# print(f'Reference of A = {sys.getrefcount(a)}')

a = [1, 2, 3]


def getrefcount(address: int) -> int:
    return ctypes.c_long.from_address(address).value


print(f'Reference count of a is {getrefcount(id(a))}')
b = a
print('b = a')
print(f'Address of B = {id(b)}')
print(f'Reference count of a is {getrefcount(id(a))}')
c = a
print('c = a')
print(f'Address of C = {id(c)}')
print(f'Reference count of a is {getrefcount(id(a))}')
c = 12
print('c = 12')
print(f'Address of C = {id(c)}')
print(f'Reference count of a is {getrefcount(id(a))}')
b = None
print('b = None')
print(f'Address of B = {id(b)}')
print(f'id of b {id(b)}')
print(f'Reference count of a is {getrefcount(id(a))}')
a_id = id(a)
a = None
print(f'Reference count of a_id is {getrefcount(id(a_id))}')
