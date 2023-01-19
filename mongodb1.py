import pymongo
import json

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

# print(mydb)

# dblist = myclient.list_database_names()
# print(dblist)

# if "mydatabase" in dblist:
#   print("The database exists.")


mycol = mydb["customers"]

# collist = mydb.list_collection_names()
# print(collist)

# if "customers" in collist:
#   print("The collection exists.")


##########################################################INSERT#########################################################

""" mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id) """

##########################################################INSERT MANY #########################################################


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

# x = mycol.insert_many(mylist)

# x = mycol.find_one()

# print(x)

########################################################## FIND #########################################################


""" data = mycol.find()
for x in data :
    # print(x['name'])
    print(x) """




""" data = mycol.find({}, {"_id":0, "name":1})
for x in data :
    print(x) """

##########################################################FILTER#########################################################


# myquery = {"name": 'Ben'}
# myquery = {"name": {"gt":'S'}}
# myquery = { "address": { "$regex": "^S" } }
# data = mycol.find(myquery)

##########################################################SORT#########################################################


# data = mycol.find().sort("name")
# data = mycol.find().sort("name", -1)

########################################################## INSERT #########################################################


# mydict = { "name": "GAURAV", "address": "HAPUR" }
# mycol.insert_one(mydict)

# data = mycol.find().sort('name')

########################################################## DELETE #########################################################


# myquery = {"name": 'GAURAV'}

# mycol.delete_one(myquery)

# x = mycol.delete_many(myquery)

# x = mycol.delete_many({})

# print(x.deleted_count, "documents deleted")

# mycol.delete_many({})


""" i=0
mylist = []
while(i<10):
    mylist.append({'name':'Gaurav Marvaha' + str(i), 'Mobile':int('888143809' + str(i))})
    i+=1 """

# print(json.dumps(mylist,indent=4))

# mycol.insert_many(mylist)


############################################# DROP COLLECTION #############################################################

# mycol.drop()

################################################## Update Document #########################################################


# myquery = {"Mobile":8881438090}

# updateQuery = {"$set": {"Mobile": 8410107875} }

# mycol.update_one( myquery, updateQuery )


""" myquery = { "name": {"$regex":"^G"} }
updateQuery = {"$set": {"Mobile": 8410107879} }

x= mycol.update_many( myquery, updateQuery )
print(x.modified_count, "documents updated.") """

###########################################################################################################################


""" mydict = { "name": "GAURAV", "address": "HAPUR" }
x= mycol.insert_one(mydict)
print(x.inserted_id) """

data = mycol.find()
# data = mycol.find().limit(2)

for x in data:
    print(x)
else:
    print('Finally Executed...')



###########################################################################################################################



















