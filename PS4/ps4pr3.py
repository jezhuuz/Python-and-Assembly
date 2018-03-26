#
# Jenna Zhu
# jennazhu@bu.edu
#
# CS111 Problem Set 4
# Problem 3 - Recusive operations on binary numbers
#

from ps4pr1 import *


def bitwise_and(b1, b2):
    ''' takes as inputs two strings b1 and b2 that represent binary numbers
        function should use recursion to compute the bitwise AND of the
        two numbers and retun the result in the form of a string
    '''

    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        and_result = (int(b2[0]) and 0)
        multiply = len(b2)
        return str(and_result) * multiply
    elif b2 == '':
        and_result = (int(b1[0]) and 0)
        multiply = len(b1)
        return str(and_result) * multiply
    else:
        rest = bitwise_and(b1[:-1], b2[:-1])
        #print('b1:', b1)
        #print('b2:', b2)
        #print('b1[-1]:', b1[-1])
        #print('b2[-1]:', b2[-1])
        and_result = int(b1[-1]) and int(b2[-1])
        #print('and_result:', and_result)
        return rest + str(and_result)



def add_bitwise(b1, b2):
    ''' adds two binary numbers.
        uses recursion to perform the bitwise addition algorithm
        returns the result.
        should NOT perform any base conversions, should NOT call
        the add_bytes function from Problem 2.
    '''

    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        rest = add_bitwise(b1[:-1], b2[:-1])
        if (int(b1[-1]) + int(b2[-1]) > 1):
            #pass the carry bit into the second recursive call
            #and add a '0' to the end of result string if 1 + 1
            carry_case = add_bitwise(rest, '1')
            return carry_case + '0'
        if int(b1[-1]) == 0 and int(b2[-1]) == 0:
            return rest + '0'
        else:
            return rest + '1'
            
