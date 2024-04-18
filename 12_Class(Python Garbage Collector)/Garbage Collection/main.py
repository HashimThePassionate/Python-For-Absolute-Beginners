import ctypes
import gc


def getrefcount(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object Exists"
    else:
        return "Object Does Not Exists"


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A : Self {hex(id(self))} b: {hex(id(self.b))}')


class B:
    def __init__(self, a):
        self.a = a
        print(f'B : Self {hex(id(self))} a: {hex(id(self.a))}')


gc.disable()
print('---------------------------------')
my_var = A()
print('---------------------------------')
print('------------------')
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))
print('------------------')
id_a = id(my_var)
id_b = id(my_var.b)
print(hex((id_a)))
print(hex((id_b)))
print('------------------')
print(getrefcount(id_a))
print(getrefcount(id_b))
print('------------------')
print(object_by_id(id_a))
print('------------------')
print(object_by_id(id_b))
print('------------------')
my_var = None
print(getrefcount(id_a))
print('------------------')
print(getrefcount(id_b))
print('------------------')
print(object_by_id(id_a))
print('------------------')
print(object_by_id(id_b))
print('------------------')
gc.collect()
print('------------------')
print(object_by_id(id_a))
print('------------------')
print(object_by_id(id_b))
print('------------------')
