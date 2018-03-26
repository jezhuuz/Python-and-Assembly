#
# name : Jenna Zhu
# email : jennazhu@bu.edu
#
# Problem Set 2
# Problem 2
#

def mirror(s):
    ''' takes a string s and returns a mirrored version of s
        that is twice the length of the original string
    '''

    mirrored = s[::-1]
    return(s + mirrored)


def is_mirror(s):
    ''' takes a string s and returns True if s is a mirrored string
        and False otherwise
    '''
    
    first_half = s[0:(len(s)//2)]
    second_half = s[(len(s)//2):]
    
    if second_half == first_half[::-1]:
        return True
    else:
        return False

def test():
    ''' this test function tests the functions above '''
    
    print('test case for mirror("bacon"):', mirror('bacon'))
    print('test case for print(mirror("XYZ"))', mirror('XYZ'))

    print('test case for is_mirror("baconnocab")', is_mirror('baconnocab'))
    print('test case for print(is_mirror("baconnoca"))', is_mirror('baconnoca'))
