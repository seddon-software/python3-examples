salary = { 
          'john' : 45000,
          'mary' : 35000,
          'susan': 61000,
          'sergi': 72000,
          'kamel': 42000
          }

salary['john'] = 46000  # update
salary['peter'] = 71000   # add new
salary['mary'] = None    # unknown value
del salary['susan']    # delete a key
# salary.pop('susan')    # delete a key
print salary

theKeys = salary.keys()
theValues = salary.values()
print theValues
