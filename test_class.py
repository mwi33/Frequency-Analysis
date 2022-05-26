class Person:
  def __init__(self, name, age, data_file):
    self.name = name
    self.age = age
    self.data_file = data_file

  def myfunc(self):
    print("Hello my name is " + self.name)

    data = open("test_data.txt")

    print(data)


p1 = Person("John", 36)
p1.myfunc() 