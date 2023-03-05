class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"
  
  def age1(self):
    return self.age + 1
  
p1 = Person("John", 36)

# print(p1)
print(p1.age1())