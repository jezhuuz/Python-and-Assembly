#
# Jenna Zhu
# jennazhu@bu.edu
#
# Problem Set 6 Problem 5
#
# The Fibonacci sequence in Python
#

def fib(n):
    ''' takes an integer n as input and then uses a loop to both:
            - determine and print the first n Fibonacci numbers
            - compute and return the sum of those numbers
        ***input n is at least 2
    '''

    sum = 0
    steps = 0
    current = 0
    fib1 = 1
    fib2 = 1

    while steps < n:
        
        if steps == 0:
            current = fib1
            sum = 1
        elif steps == 1:
            current = fib2
            sum += current
        else:
            current = fib1 + fib2
            sum += current

        print(current)
        fib1 = fib2
        fib2 = current

        steps += 1
        
    return sum

def main():
    ''' ask the user how many Fib numbers he or she wants to produce
        call fib() to generate and print those numbers
        print the sum of the numbers (i.e. value returned by fib)
    '''
    n = int(input('How many Fibonacci numbers? '))
    sum = fib(n)
    print('their sum is', sum)
