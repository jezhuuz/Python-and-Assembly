#
# Jenna Zhu
# jennazhu@bu.edu
#
# ps2pr7.py - Problem Set 2, Problem 7
#
# Fun with recursion, part II
#


def letter_score(letter):
    ''' takes a lowercase letter as input and returns the value
        of that letter as a scrabble tile.
        if letter is not lowercase from 'a' to 'z',
        function should return 0.
    '''
    
    assert(len(letter) == 1)
    
    check_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    if (letter in check_letter) == False:
        return 0
    else:
        if letter == 'a':
            return 1
        
        elif letter == 'b':
            return 2

        elif letter == 'c':
            return 3
        
        elif letter == 'd':
            return 2
        
        elif letter == 'e':
            return 1
        
        elif letter == 'f':
            return 4

        elif letter == 'g':
            return 2
        
        elif letter == 'h':
            return 4
        
        elif letter == 'c':
            return 3
        
        elif letter == 'd':
            return 2
        
        elif letter == 'e':
            return 1
        
        elif letter == 'f':
            return 4

        elif letter == 'g':
            return 2
        
        elif letter == 'h':
            return 4
        
        elif letter == 'i':
            return 1
        
        elif letter == 'j':
            return 8
        
        elif letter == 'k':
            return 5
        
        elif letter == 'l':
            return 1

        elif letter == 'm':
            return 3
        
        elif letter == 'n':
            return 1
        
        elif letter == 'o':
            return 1
        
        elif letter == 'p':
            return 3
        
        elif letter == 'q':
            return 10
        
        elif letter == 'r':
            return 1

        elif letter == 's':
            return 1
        
        elif letter == 't':
            return 1
        
        elif letter == 'u':
            return 1
        
        elif letter == 'v':
            return 4
        
        elif letter == 'w':
            return 4
        
        elif letter == 'x':
            return 8

        elif letter == 'y':
            return 4
        
        elif letter == 'z':
            return 10



def scrabble_score(word):
    ''' takes a string word containing only lowercase letters,
        uses recrusion to compute and return the scrabble score
        of that string
    '''
    
    score = 0
        
    if (word == ''):
        return score
    
    else:
        score = letter_score(word[0])
        rest = scrabble_score(word[1:])
        return score + rest


def index(elem, seq):
    ''' takes an element elem and a sequence seq
        uses recursion to find and return the index of the first
        occurrence of elem in seq.
        seq can be either a list or a string.
        if seq is string, elem will be a single-char string
        if seq is list, elem can be any value
    '''
    ''' my index(elem,seq) function is not fully functional
        it works for if the element is in the sequence,
        but does not work if the element is not in the sequence
    '''

    my_index = 0
    #print(seq)
    
    if(seq == '' or seq == []):
        return -1
    
    else:
        
        rest = index(elem, seq[1:])
        
        if (elem == seq[0]):
        #print('my_index in if elem:', my_index)
            return my_index

        elif (elem != seq[0]):
        #print('moved on')
        #print('rest:', rest)
        #print('my_index in not elem:', my_index)
            
            if(rest == -1):
                return -1
            
            return 1 + rest


def test():
    ''' test function for the functions above '''

    test1 = letter_score('w')
    print('the first test returns', test1)

    test2 = scrabble_score('python')
    print('the second test returns', test2)

    test3 = index(5, [4, 10, 5, 3, 5, 8])
    print('the third test returns', test3)

    test4 = index('b', 'banana')
    print('the fourth test returns', test4)

    test5 = index('a', 'banana')
    print('the fifth test returns', test5)
    
    test6 = index('i', 'team')
    print('the sixth test returns', test6)

    test7 = index('hi', ['hello', 111, True])
    print('the seventh test returns', test7)

    test8 = index('a', '')
    print('the eigth test returns', test8)

    test9 = index(42, [])
    print('the ninth test returns', test9)
