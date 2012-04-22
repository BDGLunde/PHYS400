#Exercise 7.1, Rewriting print_n(n) using iteration

def print_n(s,n):
    while n>0:
        print s
        n = n-1
    print 'Finished!'

print_n('Hello',5)
