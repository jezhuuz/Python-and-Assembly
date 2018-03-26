# 
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions with string inputs
#
# name: Jenna Zhu
# email: jennazhu@bu.edu
#

def replace_prefix(word, prefix):
    ''' takes a string word and a string prefix
        returns a string in which the character in prefix replace the
        characters of word (up to the length of prefix)
    '''
    
    prefix_size = len(prefix)
    word = prefix + word[prefix_size::]
    return word


def swap_halves(s):
    ''' takes a string input s and returns a string whose first half
        is s's second half and whose second half is s's first half

        if len(s) is odd, first half of input string should have one
        fewer character than the second half
    '''
    
    half_value = len(s) // 2
    first_half = s[0:half_value]
    second_half = s[half_value::]
    result = second_half + first_half

    return result


def statistics(list_of_int):
    ''' takes in a list of (exactly) 3 integers
        returns a list of the following statistics:
            sum, average value, smallest value, and largest value
    '''

    sum_value = list_of_int[0] + list_of_int[1] + list_of_int[2]
    average = sum_value / 3

    if list_of_int[0] < list_of_int[1]:
        smallest = list_of_int[0]
        if list_of_int[2] < smallest:
            smallest = list_of_int[2]
    else:
        smallest = list_of_int[1]
        if list_of_int[2] < smallest:
            smallest = list_of_int[2]

    if list_of_int[0] > list_of_int[1]:
        largest = list_of_int[0]
        if list_of_int[2] > largest:
            largest = list_of_int[2]
    else:
        largest = list_of_int[1]
        if list_of_int[2] > largest:
            largest = list_of_int[2]

    return [sum_value, average, smallest, largest]
    
