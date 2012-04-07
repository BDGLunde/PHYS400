#Exercise 3.4


def topBord(n):
    x = "+ - - - - "
    print x*(n-1)+ "+"

def print_four(s):
    print s
    print s
    print s
    print s

def do_twice(f,s):
    f(s)
    f(s)

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)

    
def cellBlock(n):
    topBord(n)
    vert = "|         "
    print_four(vert*n)

def grid2x2(f,n):
    do_twice(cellBlock,n)
    topBord(n)

def grid4x4(f,n):
    do_four(cellBlock,n)
    topBord(n)


#Number of cells is n-1 as n signifies the number of corners (+ signs). It was
# done this way because in def topBord(n), simply using x*n would create
# a remainder of 4 dashes without a + terminating them. If taken in the reverse,
# we would be left with our first left corner with no + corner.

grid4x4(cellBlock,5)  #4x4
grid2x2(cellBlock,3)  #2x2

wait_for_user()
#With some knowledge of user input, this could be easily used to create an
# arbitrary nxn sized grid. Would also probably need something similar to a
# while function to get an arbitrary sized do_n(f,s);

