class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)



""" class Student(Person):
    def printData(Person):
        print(Person.firstname)
        print(Person.lastname) """
        
        
class Student(Person):
    """ def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) """

    def printname1(self):
        print(self.firstname, self.lastname)
        
    def printname(self):
        print(self.firstname + '______' +self.lastname)
        
        
s = Student("Mike", "Olsen")
p = Person("GAURAV", "MARVAHA")

s.printname()
s.printname1()
p.printname();
