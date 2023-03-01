#Directory of .py to .py

#Import a single class from a single module in new package in python

#import square
from Square import Square

#Testing
side = 8
my_square = Square(side)
print('Area Test 1: My area is ',my_square.area())

################


#Importing a single class from a module that stores multiple classes
from Geom1 import Geom

#Testing
my_geom = Geom()
my_geom.print_name()

#################

#importing multiple classes from a module
from Geom1 import Geom, Square, Triangle

#Testing
##Triangle
base = 6
height = 7
my_triangle = Triangle(base,height)
my_triangle.print_name()
print('Area Test 2: My triangle area is ', my_triangle.area())

##Square
side = 8
my_square = Square(side)
my_square.print_name()
print('Area Test 3: My area is ',my_square.area())

#################

#Importing an entire module
from Geom1 import *

#Testing
#Circle
radius = 2
my_circle = Circle(radius)
my_circle.print_name()
print('Area Test 4:  My area is ',my_circle.area())