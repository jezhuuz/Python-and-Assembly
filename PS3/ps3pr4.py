#
# Jenna Zhu
# jennazhu@bu.edu
#
# Problem Set 3, Problem 4
# More algorithm design
#

def rem_last(elem, values):
    ''' inputs value elem and a list values and uses recursion to create
        and return a version of values in which the last occurrence
        of elem has been removed
    '''
    #print(values)
    
    if values == []:
        return []
    
    elif values[-1] == elem:
        #print('values[-1] matches')
        return values[:-1]
    
    else:
        #print('in else statement:')
        result_rest = rem_last(elem, values[:-1]) + [values[-1]]
        #print('values:', values)
        #print('result_rest', result_rest)
            
        return result_rest


def rem_first(elem, values):
    """ removes the first occurrence of elem (letter) from the string values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest


def jscore(s1, s2):
    ''' takes two strings s1 and s2 as inputs and returns the Jotto score
        of s1 compared with s2....the number of characters in s1 that are
        shared by s2.
        used rem_first function but instead of list input, has string input
    '''
    score = 0
    
    if (s1 == '') or (s2 == ''):
        return 0
    
    elif s1[0] in s2:
        score = score + 1
        return score + jscore(s1[1:], rem_first(s1[0], s2))
                              
    else:
        return score + jscore(s1[1:], s2)

def lcs(s1, s2):
    ''' takes two strings s1 and s2 and returns the longest common subsequence
        that they share
        these letters must appear in the same order in both s1 and s2 but not
        necessarily consecutively
    '''

    if (s1 == '') or (s2 == ''):
        return ''

    #if the first characters in the two strings match, include that
        #character in the LCS and process the remaining characters
    if (s1[0] == s2[0]):
        lcs_string = s1[0]
        rest = lcs(s1[1:], s2[1:])
        return lcs_string + rest
        
    #if the first characters do not match, make two recursive calls
        #one that eliminates the first character in s1, one that
        #eliminates the first character in s2
    #return the better of these two results, otherwise return either
    
    else:
        result1 = lcs(s1[1:], s2)
        result2 = lcs(s1, s2[1:])

        if len(result1) > len(result2):
            return result1
        
        elif len(result1) == len(result2):
            return result1
        
        else:
            return result2
        
        
