#!/bin/usr/python

def ruler(n, last=False):
    """ Returns a single row of size (2^n+1) with | at either ends, and blanks (or
    underscores if last=True) in the middle. """

    if last:
        return '|' + (2**n -1)*'_' + '|'
    else:
        return '|' + (2**n -1)*' '  + '|'

def row(i, n, last=False):
    """ Returns the i^th row of a n-sized ruler. """

    return (2**i)*(ruler(n-i, last)[:-1]) + '|'

def main(n):
    """ For a given n, prints out an ascii ruler of size n. """

    for i in xrange(n-1):
        print row(i, n)

    print row(n-1, n, last=True)

if __name__ == '__main__':
    main(6)

