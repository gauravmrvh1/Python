""" thislist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry"))

print(thislist)
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
list1[1] = 'HHAHA'

print(list1[1])
print(type(list1)) """




################################### Python - Access List Items##########################################


""" thislist = ["apple", "banana", "cherry"]
print(thislist[1])


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") """


####################### Python - Change List Items #####################################################


""" thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) """



##################### Python - Add List Items ##########################################################

""" thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") # touple
thisSet = {"kiwi1", "orange1"} # set
thisDict = {'key':'value', 'key1':'value1'}

thislist.extend(thistuple)
thislist.extend(thisSet)
thislist.extend(thisDict.values())
thislist.extend(thisDict.keys())

print(thislist)
 """


####################### Python - Remove List Items ###################################################

""" thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
# del thislist
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) """




###################### Python - Loop Lists ##########################################################

""" thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1 """


################ Python - Sort Lists ###############################################################

""" thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) """


""" thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) """


""" thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) """


""" thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) """


""" thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) """


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)



######################## Python - Copy Lists #####################################################

""" thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
 """


################### Python - Join Lists###########################################################

""" 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) """


""" list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) """

































