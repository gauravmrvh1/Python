""" x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z) """




""" x = y = z = "Orange"
print(x)
print(y)
print(z) """





""" fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z) """



""" x = "Python"
y = "is"
z = "awesome"
print(x, y, z) """



""" x = "Python "
y = "is "
z = "awesome"
print(x + y + z) """



# x = 5
# y = 10
# print(x + y)



# x = 5
# y = "John"
# print(x, y)


def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print("Output is: ")
    print (arg1)
    print('dunamic variable length',len(vartuple))
    for var in vartuple:
        print (var)
    return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )