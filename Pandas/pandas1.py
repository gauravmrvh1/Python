import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

print(pandas.__version__)

myvar = pandas.DataFrame(mydataset)
print(myvar)