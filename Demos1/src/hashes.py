salary = { 
          'john' : 45000,
          'mary' : 35000,
          'susan': 61000,
          'sergi': 72000,
          'kamel': 42000
          }

theKeys = salary.keys()
theKeys.sort()

for key in theKeys:
    print key, salary[key]
