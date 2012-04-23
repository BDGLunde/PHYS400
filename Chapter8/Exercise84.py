#Exercise 8.4, find


def find(word,letter,start):
    index = 0
    slice = word[start:]
    print slice
    while index<len(slice):
        if slice[index] == letter:
            return index + start
        index = index + 1
    return -1
