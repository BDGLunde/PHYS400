#Exercise 5.1. Dinking around with Fermat's Last Theorem

#Fermat's Last Theorem claims that there exists no integers a,b,c
#such that a^n + b^n = c^n for n>2.

def check_fermat(a,b,c,n):
    if n<=2 and a**n + b**n == c**n:
        print 'These should work, but keep in mind that these are exceptions.'
    elif n>2 and a**n + b**n == c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that does not work'
    
def usercheck_fermat():
    prompt = 'Enter values for integers a,b,c, and n to check if they violate Fermats Last Theorem.'
    print prompt
    prompta = 'Enter a value for integer, a\n'
    a = raw_input(prompta)
    promptb = 'Enter a value for integer, b\n'
    b = raw_input(promptb)
    promptc = 'Enter a value for integer, c\n'
    c = raw_input(promptc)
    promptn = 'Enter a value for power integer, n\n'
    n = raw_input(promptn)
    (a,b,c,n) = int(a),int(b),int(c),int(n)
    check_fermat(a,b,c,n)

usercheck_fermat()
