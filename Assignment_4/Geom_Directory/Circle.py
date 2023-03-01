class Circle():
  
  def __init__ (self,radius):
    #self.radius = radius
    super().__init__()
    self.radius = radius

  # area method  
  def area(self):
     import math as mth
     return mth.pi * self.radius **2
     