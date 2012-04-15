#Exercise 5.2, "Can I make a triangle out of these three sticks?"

#"If any of the three lengths is greather than the sum of the other two
#then you cannot form a triangle. Otherwise, you can."

def is_triangle(a,b,c):
    """Takes three integers, (a,b,c), and checks if a triangle
    can be formed using these as its legs by comparing whether or not
    any of the legs is greater than the sum of the other two
    """
    if a>b+c or b>a+c or c>a+b:
        print 'You cannot form a triangle from these lengths'

    elif a==b+c or b==a+c or c==a+b:
        print 'This combination of lengths will form a degenerate triangle.'

    else:
        print 'A triangle will be formed from this combination of lengths.'

def user_triangle():
    prompt = 'Your goal is to construct a triangle. This is a life and death situation. Choose three stick integer lengths such that you may live.'
    prompta = 'Choose an integer length for your first stick.\n'
    promptb = 'Choose another integer length.\n'
    promptc = 'Choose your final integer length.\n'

    print prompt
    a = int(raw_input(prompta))
    b = int(raw_input(promptb))
    c = int(raw_input(promptc))
    is_triangle(a,b,c)

user_triangle()
