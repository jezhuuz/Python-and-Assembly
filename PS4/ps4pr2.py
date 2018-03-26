#
# Jenna Zhu
# jennazhu@bu.edu
#
# CS111: Problem Set 4, Problem 2
#

from ps4pr1 import *


def mul_bin(b1, b2):
    ''' takes as inputs two strings b1 and b2 that represent binary numbers
        should multiply the numbers and return the result in the form of
        a string that represents a binary number
    '''

    dec_b1 = bin_to_dec(b1)
    dec_b2 = bin_to_dec(b2)
    
    answer = dec_b1 * dec_b2
    bin_answer = dec_to_bin(answer)
    
    return bin_answer


def add_bytes(b1, b2):
    ''' takes as inputs two strings b1 and b2 that represent bytes
        function should compute the sum of the two bytes
        returns that sum in the form of a string that represents a
        8-bit bniary number
    '''

    dec_b1 = bin_to_dec(b1)
    dec_b2 = bin_to_dec(b2)
    
    ans = dec_b1 + dec_b2
    bin_ans = dec_to_bin(ans)
    bin_len = len(bin_ans)

    if (bin_len < 8):
        #print('bin_len < 8')
        num_zeros = 8 - bin_len
        #print('add', num_zeros, 'many 0s')
        bin_ans = ('0' * num_zeros) + bin_ans
    else:
        #print('bin_len > 8')
        #print('print 8 rightmost 8 bits')
        num_index = bin_len - 8
        bin_ans = bin_ans[num_index:bin_len]

    return bin_ans
