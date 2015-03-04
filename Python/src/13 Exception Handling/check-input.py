def getData():
    try:
        x = raw_input("Enter integer: ")
        x = int(x)
    except ValueError, ptr:
        raise Exception("Error: " + x)
    return x


try:
    result = getData()
except Exception, e:
    print e

1