

""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) """


""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1) """




""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    # return f"{self.name}({self.age})"
    return f"{self.name}"

p1 = Person("John", 36)
print(p1) """





""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  """



""" class Person:
  def __init__(self, *arg):
    print(len(arg))
    self.name = arg[0]
    self.age = arg[1]

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
print(p1.age)
p1.age = 40
# del p1
print(p1.age) """





class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

######################################################################################

class MyClass:
  x = 10
  def __init__(self, *arg):
    self.arg1 = arg[0]
    self.arg2 = arg[1]
  
  def response(self):
    self.newProp = 'Gaurav Marvaha' # here we're adding new prop
    print(self.arg1)
    print(self.arg2)
  
obj = MyClass(10,20)
# print(obj.x)
obj.response()
print(obj.newProp)

########################################################################################



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


########################################################################################






























































