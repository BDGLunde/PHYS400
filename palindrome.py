#Exercise 6.6 - Palindromes

from math import *


def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    
    if len(word)==1:
        return True
    if len(word)==2:
        if first(word)==last(word):
            return True
        else:
            return False
    if is_palindrome(middle(word))==True and first(word)==last(word):
        return True
    else:
        return False
   
    


print is_palindrome('ab')
