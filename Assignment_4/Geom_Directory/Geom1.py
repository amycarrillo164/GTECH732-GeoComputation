import math as mth
import random

import os
directory = "Geom_Directory"
#parent_dir = r"C:\Users\amyca\GTECH-HW\Assignment_4"
#path = os.path.join(parent_dir, directory)
#os.mkdir(path)
#print("Directory '% s' created" % directory)


class Geom():
  import random
  geomType = 'Generic Geometry Type'
  
  # Constructor of the class: used to initialize an object
  def __init__(self):
    # Check out the names and the faker packages for random names
    self.name = random.choice(['Bill','Sally','Tamica','Josh','Lammar','Hussain'])
    self.color = random.choice(['BLUE', 'RED', 'PURPLE'])
  
  def print_name(self):
    print('My name is ',self.name, 'and my color is ',self.color)

  def makeString(self):
    return f"Name: {self.name}, Color: {self.color}, Area: {self.area()}"

class Circle(Geom):
  
  def __init__ (self,radius):
    self.radius = radius
    super().__init__()

  # area method  
  def area(self):
     return mth.pi * self.radius **2

class Square(Geom):
  
  def __init__ (self,side):
    self.side = side
    super().__init__()
  # area method  
  def area(self):
     return self.side **2

class Triangle(Geom):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()

    #area method
    def area(self):
        return (self.base * self.height)*0.5
    

