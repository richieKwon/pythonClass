# # Data model

# Sequence / Iterator / Function / Class
from collections import namedtuple
from math import sqrt
a = 7
# print(id(a)) id vs value
print(type(a))
# print(dir(a))

# NamedTuple
Point = namedtuple('Point', 'x y')
point1 = Point(1.0, 5.0)
point2 = Point(2.5, 1.7)

length = sqrt(
    (point1.x-point2.x)**2 +
    (point1.y-point2.y)**2
)
print(length)

# temp dict
temp_location_dic = {'x': 7, 'y': 7}

# Declare namedtuple
Location = namedtuple('Location', ['x', 'y'])
print(Location(**temp_location_dic))

location = Location(7, 7)
print(location[0] + location[1])
print(location.x + location.y)

# method for namedtuple make()
location2 = location._make([8, 8])
print(location2)

# checking the field names
print(location._fields)

# _asdict() : return values as OrderedDict
print(location._asdict())

# _replace : return values replaced
print(location._replace(y=100))
