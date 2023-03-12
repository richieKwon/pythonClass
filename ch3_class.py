class Student(object):
    '''
    Student Class
    author: richie
    description: walk through how to create instance method or static method
    '''

    # Class variable
    tuitionFeeRate = 1.0

    def __init__(self, id, firstName, lastName, email, grade, tuitionFeeRate, gpa):
        self._id = id
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._grade = grade
        self._tuitionFeeRate = tuitionFeeRate

    # instance method
    def fullName(self):
        return '{},{}'.format(self._firstName, self._lastName)

    def detailInfo(self):
        return '{}, {}'.format(self.fullName(), self._email)

    # Class method
    @classmethod
    def raiseFeeRate(cls, per):
        if per <= 1:
            print('Enter over 1')
            return
        cls.tuitionFeeRate = per
        print('The tuition fee rate has gone up!')

    # create a instance with class method
    @classmethod
    def createNewStudent(cls, id, firstName, lastName, email, grade, tuitionFeeRate, gpa):
        return cls(id, firstName, lastName, email, grade, tuitionFeeRate, gpa)

    # create a static method
    @staticmethod
    def isScholarship(instance):
        if instance._gpa >= 4.1:
            return '{} is entitled to have a scholarship'.format(instance._lastName)
        else:
            return '{} is NOT entitled to have a scholarship'.format(instance._lastName)


# change class variable with classmethod
Student.raiseFeeRate(1.7)

student7 = Student.createNewStudent(
    7, 'Lee', 'Jennifer', 'newzeland@gmail.com', 'A', 1, 4.0)


# run staticmethod
print(Student.isScholarship(student7))
print(student7.isScholarship(student7))
