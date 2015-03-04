############################################################
#
#    exceptions
#
############################################################

def square(x):
    """
    This function squares a number
    >>> square(-3)
    9
    >>> square(16)
    Traceback (most recent call last):
    ...
    ValueError: input too large
    """
    if x > 10:
        raise ValueError('input too large')
    else:
        return x*x


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)

1

