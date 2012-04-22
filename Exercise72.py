#Exercise 7.2, Square roots


def square_root(a):
    x = 0.75*a
    epsilon = 0.00000000001
    while True:
        print x
        y = (x+ a/x) /2
        if abs(y-x) < epsilon:
            break
        x = y


square_root(100)
