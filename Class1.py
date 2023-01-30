

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





""" class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage() """

######################################################################################

""" class MyClass:
  x = 10
  def __init__(self, *arg):
    self.arg1 = arg[0]
    self.arg2 = arg[1]
    print(MyClass.x)
    MyClass.x = 1000
  
  def response(self):
    # here we're adding new prop
    MyClass.newProp = 'Gaurav Marvaha' 
    self.newProp = 'Gaurav MARVAHA' 
    print(self.arg1)
    print(self.arg2)
  
obj = MyClass(10,20)
print(obj.x)
obj.response()
print(obj.newProp)
print() """

########################################################################################



""" class Person:
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
x.welcome() """


########################################################################################


""" class Parent:
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)
      
class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr() """


########################################################################################



class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
print(v1)
v2 = Vector(5,-2)
print(v2)
print (v1 + v2)



########################## DATA HIDING ##############################################################


class JustCounter:
  __secretCount = 0
  
  def count(self):
    self.__secretCount += 1
    print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print (counter.__secretCount)
print(counter._JustCounter__secretCount)



































