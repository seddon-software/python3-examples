############################################################
#
#    failures
#
############################################################

def square( x ):
    """
    This function squares a number
    >>> square(-3)
    9
    >>> square(16)
    256
    """
    if x > 10:
        return 0
    else:
        return x*x

def sumsquares(n):
    """
    This computes the sum of squares from 1 to n
    >>> sumsquares( 2 )
    5

    1+4+9 = 14
    >>> sumsquares( 3 )
    14

    1+4+9+16 
    >>> sumsquares( 4 )
    30457
    
    >>> sumsquares( 0 )
    0
    >>> sumsquares( -1 )
    'Error'
    """
    if n < 0:
        return "Error"
    sum = 0
    for i in range(n+1):
        sum += square(i)
    return sum

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)

1
