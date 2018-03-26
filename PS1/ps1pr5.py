# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions with string inputs
#
# name: Jenna Zhu
# email: jennazhu@bu.edu
#

def front3(s):
    ''' takes an input string s and returns a new string
        which is 3 copies of the front (first 3 chars of the string)
        if string length < 3, front is whatever is there
    '''
    
    print(len(s))
    
    if len(s) < 3:
        return(s * 3)
    else:
        front = s[0:3]
        return(front * 3)

    
def shorter_len(l1, l2):
    ''' takes as inputs two lists l1 and l2
        and returns the length of te shorter of the two lists
    '''
    
    l1_length = len(l1)
    l2_length = len(l2)
    
    if l1_length < l2_length:
        return l1_length
    else:
        return l2_length

def ends_with(word, suffix):
    ''' takes two string values word and suffix
        returns True if the string word ends with the suffix
        returns False otherwise
    '''
    
    word_size = len(word)
    suffix_size = len(suffix)
    last_index = word_size
    first_index = last_index - suffix_size
    end = word[first_index:last_index]

    if end == suffix:
        return True
    else:
        return False

    
    
