#
# Jenna Zhu
# jennazhu@bu.edu
# 
# ps2pr6.py - Problem Set 2, Problem 6
#
# list comprehensions
#

# Problem 6-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [x*2 for x in range(5)]
print(lc1)

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1] for w in words]
print(lc2)

# part c
lc3 = [(word[::-1]*2) for word in ['hello', 'bye', 'no']]
print(lc3)

# part d
lc4 = [x**2 for x in range(1, 10) if (x % 2 == 0)]
print(lc4)

# part e
lc5 = [(c == 'b' or c == 'u') for c in 'bu be you']
print(lc5)




# Problem 5-2: Put your definition of the powers_of() function below.


def powers_of(base, count):
    ''' takes a number base and a positive integer count
        uses list comprehension to construct and return a list
        containing the first count powers of base,
        beginning with the 0th power
    '''
    
    x = base
    y = count
    powers_list = [x**y for y in range(0,y)]
    return(powers_list)



# Problem 5-3: Put your definition of the shorter_than() function below.


def shorter_than(n, wordlist):
    ''' takes an integer n and a list of strings wordlist
        uses a list comprehension to construct and return a list
        consisting of all words from wordlist shorter than n
    '''

    max_len = n
    shorter_list = [x for x in wordlist if (len(x)< n)]
    return(shorter_list)
    


