#!/usr/bin/python
''' Solution to the Farmers' elevation problem'''

class Tile:
    '''Defines a Tile class which contains the co-ordinates of the cell, along with its
    height'''

    def __init__(self, x, y, ht):
        '''Default constructor for Tile Class'''
        self.x = x
        self.y = y
        self.ht = ht
        self.minNbr = None

    def setminNbr(self, mNbr):
        '''Sets the minNbr variable'''
        self.minNbr = mNbr

    def getSink(self):
        '''Returns the Sink corresponding to self'''
        curr = self
        if not curr.minNbr:
            return curr
        else:
            return curr.minNbr.getSink()
            
def nbrs(i, j, els):
    '''Returns all Tiles neighboring to (i,j). 
    Current implementation returns top, bottom, right and left tiles. '''
    ns = []
    for temp in [els[i][iy] for iy in [j-1, j+1] if 0<= iy< n]:
        ns.append(temp)
    for temp in [els[ix][j] for ix in [i-1, i+1] if 0<= ix< n]:
        ns.append(temp)
    return ns

def FlowsTo(i, j, els):
    '''Returns the Tile to which water flows from the current Tile'''
    minT = min(nbrs(i, j, els), key=lambda T:T.ht)
    if els[i][j].ht > minT.ht:
        return minT
    else:
        return None

if __name__ == '__main__':
    
    import sys
    from collections import Counter

    try:
        datafile = sys.argv[1]
        # Input data
        f = open(sys.argv[1], 'r')
        n = int(f.readline())
        hts = []
        for line in f:
            hts.append(map(int, line.strip().split(' ')))
        f.close()
        
        # Construct an array of Tiles from the input data
        els = [[[] for i in range(n)] for i in range(n)]
        for i in xrange(n):
            for j in xrange(n):
                els[i][j] = Tile(i, j, hts[i][j])

        # Calculate the direction of water flow for each cell 
        for i in xrange(n):
            for j in xrange(n):
                els[i][j].setminNbr(FlowsTo(i, j, els))

        # Find corresponding sink for each cell
        sinks = []
        for i in xrange(n):
            for j in xrange(n):
                s = els[i][j].getSink()
                sinks.append((s.x, s.y))

        # Use built-in Counter function to output sizes of the basin
        for values in Counter(sinks).values():
            print values,
        print

    except:
        print 'Something went wrong!'





