#!/usr/bin/python

def populate_last_row(n):
    """ Populates the last row for a size n ruler."""

    row = []
    for i in xrange(2**n+1):
        if i%2==0:
            row.append('|')
        else:
            row.append('_')

    return row

def populate_prev_row(row, n):
    """ This function is used to populate rows bottom up. The i^th row is populated using
    the (i+1)^st row. """

    newrow = []
    first_vert = True
    for i in xrange(2**n+1):
        if row[i] == '|':
            if first_vert:
                newrow.append('|')
                first_vert = False
            else:
                newrow.append(' ')
                first_vert = True
        else:
            newrow.append(' ')

    return newrow

def main(n):
    """ For a given n, prints out an ascii ruler of size n. """

    all_rows = []
    all_rows.append(populate_last_row(n))
    for i in xrange(1, n):
        all_rows.append(populate_prev_row(all_rows[i-1], n))

    for row in all_rows[::-1]:
        print ''.join(row)

