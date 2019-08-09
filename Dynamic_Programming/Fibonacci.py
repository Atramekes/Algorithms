# !/usr/bin/python
# Algorithms
# @Author: Kortez
# @Email: 595976736@qq.com

import sys
import test_Dynamic_Programming

def Fibonacci(n):
    """ Solve Fibonacci problem.
        @params n (int): the input of the problem
        @returns the n-th fibonacci number
    """

    ### TODO - finish the function to compute the n-th fibonacci number
    ### YOUR CODE HERE
    
    ### END YOUR CODE

def run():
    ### finish this function to see your outputs (optional)
    return

if __name__ == '__main__':
    args = sys.argv[1]
    if args == "run":
        run()
    elif args == "test":
        test_Dynamic_Programming.test_Fibonacci()
    else:
        raise RuntimeError('invalid run mode')