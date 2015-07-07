############################################################
#
#    decorators
#
############################################################

def bold(fn):
    def decorate():
        # surround with bold tags before calling original function
        return "<b>" + fn() + "</b>"
    return decorate


def uk(fn):
    def decorate():
        # swap month and day
        fields = fn().split('/')
        date = fields[1] + "/" + fields[0] + "/" + fields[2]
        return date
    return decorate
    
import datetime
def getDate():
    now = datetime.datetime.now()
    return "%d/%d/%d" % (now.day, now.month, now.year)

@bold
def getBoldDate(): 
    return getDate()

@uk
def getUkDate():
    return getDate()

@bold
@uk
def getBoldUkDate():
    return getDate()


print getDate()
print getBoldDate()
print getUkDate()
print getBoldUkDate()
# what is happening under the covers
print bold(uk(getDate))()

1
