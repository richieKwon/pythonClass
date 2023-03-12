class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'repr: {}'.format(self._name)


student1 = Student('Sukie', 1, 1, {'gender': 'male', 'math': 100})
student2 = Student('Ryan', 2, 7, {'gender': 'female', 'math': 90})
student3 = Student('Kevin', 3, 3, {'gender': 'female', 'math': 10})
student4 = Student('Fredy', 4, 21, {'gender': 'male', 'math': 89})

print(student2.__dict__)
