#!/usr/bin/python3
class Fish:
  def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
    self.first_name = first_name
    self.last_name = last_name
    self.skeleton = skeleton
    self.eyelids = eyelids
  
  def swim(self):
    print("The fish is swimming")
  
  def swim_backwards(self):
    print("The fish can swim backwards")
  
class Trout(Fish):
  pass

class Clownfish(Fish):

  def live_with_anemone(self):
    print("The clownfish is coexisting with sea anemone.")

class Shark(Fish):
  def __init__(self, first_name, last_name="Shark", skeleton="Cartilage", eyelids=True):
    self.first_name = first_name
    self.last_name = last_name
    self.skeleton = skeleton
    self.eyelids = eyelids
  
  def swim_backwards(self):
    print("The shark cannot swim backwards, but can sink backwards.")

terry = Trout("Terry")
print(terry.first_name+" "+terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

casey = Clownfish("Casey")
print(casey.first_name+" "+casey.last_name)
print(casey.skeleton)
print(casey.eyelids)
casey.swim()
casey.swim_backwards()
casey.live_with_anemone()

baby = Shark("Baby")
print(baby.first_name+" "+baby.last_name)
print(baby.skeleton)
print(baby.eyelids)
baby.swim()
baby.swim_backwards()