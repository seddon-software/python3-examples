############################################################
#
#    simple example
#
############################################################

def cube(x):
    """
    The cube function returns   x * x * x
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    """
    return x*x*x

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)

1
