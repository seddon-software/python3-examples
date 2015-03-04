############################################################
#
#    formatting
#
############################################################

def minmax(x):
    """
    This function finds the min and max values in the array x
    >>> minmax([2,13,19,8])         
    (2, 19)
    >>> minmax([21,12])
    (12, 21)
    """
    return (min(x), max(x))

def squares(a, b):
    """
    returns all the squares in range a..b
    >>> squares(1,10)  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 4,    ..., 100]
    """
    answer=[]
    for i in range(a,b+1):
        answer.append(i*i)
    return answer

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)

1
