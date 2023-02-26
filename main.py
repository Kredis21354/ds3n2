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

my_pet = Dog('Zorro', 3)
me = Person('Dmytro', 180)
friend = Person('Anton', 178)

print(friend.is_sad)

my_pet.play_w_human(friend)

print('Друг сумний -', friend.is_sad)
print(friend.is_sad)

my_pet.play_w_human(me)

print(me.is_sad)
print('Я сумний -', me.is_sad)
print(me.is_sad)
