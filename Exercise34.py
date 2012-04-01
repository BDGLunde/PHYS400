#Exercise 3.4




def do_twice(f,s):
    f(s)
    f(s)

def print_twice(s):
    print s
    print s


hello = 'HelloSpam'

do_twice(print_twice,hello)
print #adds an empty row to clarify between output of do_four at bottom.

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)

do_four(print_twice,hello)

