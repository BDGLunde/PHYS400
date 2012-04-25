#Exercise 8.9, re-writing the is_palindrome(word) function using the string tools.



def is_palindrome(word):
    first = word[0].upper()
    new_word = first+word[1:]
    if word == word[::-1]:
        print new_word+' is a palindrome!'
    else:
        print new_word+ ' is not a palindrome!'

    
is_palindrome('civic')
