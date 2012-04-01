#Exercise 3.1

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I cut down trees. I eat my lunch."
    print "I go to the lavatory."



repeat_lyrics()



#No error messages when run in cmd. I suppose this means that when a function
#is being defined by calling on soon-to-be functions, it patiently waits
#for said functions to be defined. As a test, I removed the def print_lyrics():
#and the resulting error is 'NameError: global name 'print_lyrics' is not
#defined'.
