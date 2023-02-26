class Person:
  height = 170
  name = "Name"
  is_sad = True
  def __init__(self, name, height):
    self.name =  name
    self.height = height

class Dog:
  color = 'Grey'
  age = 3
  name = "Name"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def play_w_human(self, human):
    human.is_sad = False 


