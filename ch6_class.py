# Magic method
n = 100
print(n.__add__(7))


class Employee:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return f"emplolyee infomation -  {self._name} & {self_height}"


e1 = Employee('Fred', 190)
e2 = Employee('Jon', 200)
