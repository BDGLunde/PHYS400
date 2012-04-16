#Exercise 6.6 - Palindromes

from math import *


def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

civic = 'civic'

#print first(civic)
#print last(civic)
#print middle(civic)




def is_palindrome(word):
    """Takes a word as input and checks if it is a palindrome.
    """
    if len(word) == 1:
        return True
    
    if len(word)==2:              #For words with an even number of letters
        if first(word) == last(word):
            return True
        else:
            return False

    if is_palindrome(middle(word)) and first(word)==last(word):
        return True
    else:
        return False
                
print is_palindrome('radar')
