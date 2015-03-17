############################################################
#
#    dictionary
#
############################################################

# set up a dictionary
salary = {
 		  "zak":   34000, 
          "sara":  27000,
          "pedro": 52000,
          "kilas": 12500,
          "zoe":   66000
         }
salary["sara"] = 28000
salary["george"] = 37000


mylist = salary.keys()
mylist.sort()

for key in mylist:
    print key, salary[key]
    
     
1
