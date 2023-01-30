class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
 
 
try:
    raise(MyError(3*2))
 
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)
    
    
    
    
    
    
    
    
    
    
    
# # define Python user-defined exceptions
# class Error(Exception):
# 	"""Base class for other exceptions"""
# 	pass

# class zerodivision(Error):
# 	"""Raised when the input value is zero"""
# 	pass

# try:
# 	i_num = int(input("Enter a number: "))
# 	if i_num == 0:
# 		raise zerodivision
# except zerodivision:
# 	print("Input value is zero, try again!")




# for i in range(0):
#    print(i)
   
   
   
# i = 1
# while True:
#     if(1%2==0):
#         break
#     print(i)
# i += 2
   
print(~~~~~19) # -20

print('raining'. find('z'))

b = [11,13,15,17,19,21]

print(b[::2])

print(max("please help ")) #s


def f():
   pass
print(type(f()))

s = {3, 4, 1, 2}

print(len(s))
print(max(s))

print(type(1/2))


""" string = "Tutorials Point is best"
for i in ' '.join(string.split()):
   print(i, end= ". ")
 """

print('Tutorials Point' [100:200])


colors = ["white", "Black", "Grey "]
x = "Red" not in colors
print(x)



n =(m for m in range(3))
for m in n:
   print(m)
   
for m in n:
   print(m)




q =( 'a', 'b')
print(3 * q)





""" d0 = { 'a':1, 'b':2}
d1 = { 'a':3, 'b':4}
print( d1 > d0 ) """



def main(): 
   try: 
      func() 
      print("print this after function call") 
   except ZeroDivisionError: 
      print('Divided By Zero! Not Possible! ') 
   except: 
      print('Its an Exception!') 
      
def func(): 
   print(1/0) 
   
main()




# l = [1,2,6,5,7,8]
# l.insert(9)
# print(l) # error




a, b = c = 2 + 2, "TutorialsPoint"

print(a)
print(b)
print(c)


minidict = { 'name': 'TutorialsPoint', 'name': 'website'}
print(minidict['name'])


L = [1,2,3]

print(L[-2])




a,b = xx  = 'gaurav', 'ankit'
print(a)
print(b)
print(xx)















