#Exercise 7.4, eval_loop

def eval_loop():
    
    """Takes a mathematical operation from user input as a string and evaluates it as an int or float.
    After evaluation, the result is displayed. When 'done' is the input, the loop terminates.
    """
    
    while True:
        line = raw_input('Enter a mathematical operation for evaluation: ')
        if line == 'done':
            break
        result = eval(line)
        print result
        
    print 'Done!'

eval_loop()

