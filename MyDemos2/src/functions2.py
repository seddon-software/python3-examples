def average(*args):  # the * wraps all inputs into a tuple
    print(sum(args) / len(args))


x = (3, 6, 7)
average(3, 6, 7)
average(3, 6, 7, 6, 2)
average(*x, 6, 2) # the * unwraps the tuple
average(6, 2, *x) # the * unwraps the tuple
