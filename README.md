# Coding-Problems

My attempts at solving some problems often asked in interviews/coding competitions.

##ASCII Ruler: 
    For a given integer n, print out an ascii ruler.
        
        For ex. - n = 1: |_|

                  n = 2: |   |
                         |_|_|

                  n = 3: |       |
                         |   |   |
                         |_|_|_|_|

##Elevation Problem: 
    I found this problem on the [careercup
    website](http://www.careercup.com/page?pid=palantir-technology-interview-questions). 

    You have been given a grid with elevation data--each cell has some given height. If a
    cell's _four_ neighboring cells all have heigher heights, then this cell is defined to
    be a sink. Water collects in sinks. If the current cell is not a sink, then water will
    flow to the neighboring cell with the lowest height.

    If a cell is
    not a sink, you may assume it has a unique lowest neighbor and that this neighbor will be
    lower than the cell. 

    Cells that drain into the same sink – directly or indirectly – are said to be part of the
    same basin. 

    The problem is to partition the map into basins. Given a map of
    elevations, partition the map into basins and output the sizes of the
    basins, in descending order. 

    Assume the elevation maps are square. Input will begin with a line with one integer, S,
    the height (and width) of the map. The next S lines will each contain a row of the map,
    each with S integers – the elevations of the S cells in the row. Some farmers have small
    land plots such as the examples below, while some have larger plots. However, in no case
    will a farmer have a plot of land larger than S = 5000. 

    The code should output a space-separated list of the basin sizes, in descending order.

    A few examples are below. 

        Input: 
        3 
        1 5 2 
        2 4 7 
        3 6 9 

        Output: 
        7 2 

        The basins, labeled with A’s and B’s, are: 
        A A B 
        A A B 
        A A A 


        Input: 
        5 
        1 0 2 5 8 
        2 3 4 7 9 
        3 5 7 8 9 
        1 2 5 4 2 
        3 3 5 2 1 

        Output: 
        11 7 7 

        The basins, labeled with A’s, B’s, and C’s, are: 
        A A A A A 
        A A A A A 
        B B A C C 
        B B B C C 
        B B C C C 


        Input: 
        4 
        0 2 1 3 
        2 1 0 4 
        3 3 3 3 
        5 5 2 1 

        Output: 
        7 5 4 

        The basins, labeled with A’s, B’s, and C’s, are: 
        A A B B 
        A B B B 
        A B B C 
        A C C C
