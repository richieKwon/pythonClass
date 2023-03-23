class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)  # __ means private
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # generator

    @property  # getter
    def x(self):
        return self.__x

    @x.setter  # setter - needs to have the same name as getter
    def x(self, v):
        self.__x = float(v)

    @property  # getter
    def y(self):
        return self.__y

    @x.setter  # setter - needs to have the same name as getter
    def y(self, v):
        if v < 30:
            raise ValueError('needs to be over 30')
        self.__y = float(v)


v = VectorP(20, 40)

# print(v.__x, v.__y)  # __ vs _ ?

for val in v:
    print(val)

print(v.x)

v.y = 70

print(v._VectorP__x)
