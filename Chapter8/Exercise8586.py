#Exercise 8.5 and 8.6, letter counter


def counter(word,searchLetter,start):
    """Slices a word at the desired index and counters how many times
    a specific letter in the slice occurs
    """
    count = 0
    slice = 'test'
    slice = word[start-1:]
    print slice
    for char in slice:
        if char == searchLetter:
            count = count+1
    print count

    
