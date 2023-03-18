# Magic method
n = 100
print(n.__add__(7))


class Employee:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return f"employee information -  {self._name} & {self_height}"


e1 = Employee('Fred', 190)
e2 = Employee('Jon', 200)


class Vector(object):
    def __init__(self, *args):
        ''' Creating a vector v = Vector(1,2) '''
        if len(args) == 0:
            self._x, self_y = 0, 0
        else:
            self._x, self_y = args

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'


v1 = Vector(3, 5)
print(Vector.__init__.__doc__)
print(v1)
