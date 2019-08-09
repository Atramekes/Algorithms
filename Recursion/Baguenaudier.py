# !/usr/bin/python
# Algorithms
# @Author: Kortez
# @Email: 595976736@qq.com

import sys
import test_Recursion

outputs = []

def flip(seq, func):
    """ Process a one/zero sequence seq according to func.
        @param seq (list[int]): the unprocessed sequence 
        @param func (int): to do which function
        @returns ~ (designed by yourself) 
    """
    ### TODO - calculate the processed_seq according to func
    ### YOUR CODE HERE (optional)
    
    ### END YOUR CODE

def Baguenaudier(n):
    """ Solve Baguenaudier problem.
        @params n (int): dimension of the problem
        @returns solution (list[int]): the list of functions to solve the problem
    """

    ### TODO - finish the function to Baguenaudier Hanoi problem
    ### YOUR CODE HERE
    

    ### END YOUR CODE
    return solution

def run():
    ### finish this function to see your outputs (optional)
    ###     use flip() (optional)
    return

if __name__ == '__main__':
    args = sys.argv[1]
    if args == "run":
        run()
    elif args == "test":
        test_Recursion.test_Baguenaudier()
    else:
        raise RuntimeError('invalid run mode')
