############################################################ 
#
# various ways of sorting using the sorted function
#
############################################################ 

def basicSorting():
    weekdays = [ "monday", "Tuesday", "wednesday", "Thursday", "friday", "Saturday", "sunday"]
    print sorted(weekdays)

def sortingWithAKey():
    weekdays = [ "monday", "Tuesday", "wednesday", "Thursday", "friday", "Saturday", "sunday"]
    print sorted(weekdays, key=str.lower)

def sortingDictionaryUsingAKeyAndFunction():
    salary = {
              "tim": 27000,
              "zak": 34000, 
              "jon": 52000,
              "sue": 12500,
              "zoe": 46000
             }
    def getSalary(key): 
        return salary[key]
    
    for key in sorted(salary, key=getSalary):
        print key, salary[key],
    print

def sortingDictionaryUsingAKeyAndLambda():
    salary = {
              "tim": 27000,
              "zak": 34000, 
              "jon": 52000,
              "sue": 12500,
              "zoe": 46000
             }
    for key in sorted(salary, key=lambda key:salary[key]):
        print key, salary[key],
    print
    
def usingACompareFunction():
    def numeric_compare(x, y):
            return x - y
    print sorted([5, 2, 4, 1, 3], cmp=numeric_compare)

####################################################################

basicSorting()
sortingWithAKey()
sortingDictionaryUsingAKeyAndFunction()
sortingDictionaryUsingAKeyAndLambda()
usingACompareFunction()
