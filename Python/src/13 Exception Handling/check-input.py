def getData():
    try:
        x = input("Enter integer: ")
        x = int(x)
    except ValueError as ptr:
        raise Exception("Error: " + x)
    return x


try:
    result = getData()
except Exception as e:
    print(e)

1