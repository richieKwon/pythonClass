class Student():
    """
    Student
    author: richie
    description : teaching materials to Garfield primary school in London
    """

#   declare a class variable for this class
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # instance variables
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email
        Student.student_count += 1

    def __str__(self):
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'repr: {}'.format(self._name)

    def detail_info(self):
        print('current Id : {}'.format(id(self)))
        print('student detail info: {} {} {}'.format(
            self._name, self_email, self_details))

    def __del__(self):
        Student.student_count -= 1


student1 = Student('Kieran', 2, 3, {'Math': 100})
student2 = Student('Kevin', 2, 3, {'Math': 100})
print(id(student1))

# comparing id (or reference)
print(student1 is student2)

# dir vs __dict__ (dictionary can display values)
print(dir(student1))
print(student1.__dict__)

# docString
print(Student.__doc__)

# display the class that a instance belong to
print(student1.__class__)
print(id(student1.__class__) == id(student1.__class__))

# access the class variables (any instance can access student_count which is 2)
# searching instance > class > parents class
print(student1.student_count)
print(student2.student_count)
print(Student.student_count)
