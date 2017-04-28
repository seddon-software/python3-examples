class UnrecoverableError(Exception): pass
class MyException(Exception): pass

def main():
    try:
        part1()
        part2()
        part3()
        part4()
    except UnrecoverableError as e:
        print("UnrecoverableError")
    except MyException as e:
        print("that's all folks")
        
def part1():
    try:
        raise MyException("oops")
        print("part 1")
    except MyException as e:
        # log it
        print(e)
        raise

def part2():
    try:
        print("part 2")
    except MyException as e:
        print(e)

def part3():
    try:
        raise UnrecoverableError("oops")
        print("part 3")
    except MyException as e:
        print(e)

def part4():
    try:
        print("part 4")
    except MyException as e:
        print(e)

main()
