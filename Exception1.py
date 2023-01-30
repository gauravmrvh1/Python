# try:
#   print(x)
# except:
#   print("An exception occurred")




# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")



# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")




# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")



# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")



# x = "hello"
# # if not type(x) is int:
# if type(x) is not int:
#   raise TypeError("Only integers are allowed")





# try:
#   # fh = open("testfile", "w")
#   fh = open("testfile", "r")
#   fh.write("This is my test file for exception handling gaurav marvaha!!")
# except IOError:
#   print ("Error: can\'t find file or read data")
# else:
#   print ("Written content in the file successfully")
#   fh.close()
# finally:
#   print('This would always be executed.')


import datetime

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!! " + str( datetime.datetime.now() ) )
   finally:
      print ("Going to close the file")
      fh.close()
except IOError:
   print ("Error: can\'t find file or read data")




def temp_convert(var):
  try:
    # return int(var)
    raise "Invalid level!"

  except "Invalid level!":
    print('invalid')
  # except ValueError, Argument:
    # print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")






























