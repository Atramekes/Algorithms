# !/usr/bin/python
# Algorithms
# @Author: Kortez
# @Email: 595976736@qq.com

import sys
import test_Recursion

outputs = []

def move(src, dst):
    """ Move a disk from src to dst.
        @param src (int): from which needle to move 
        @param dst (int): to move to which needle
        @returns none
    """
    outputs.append((src, dst))

def Hanoi(n, src, dst, tmp): ### ADD YOUR PARAMETERS
    """ Solve Hanoi problem.
        @params ? (defined by yourself)
        @returns none
    """

    ### TODO - finish the function to solve Hanoi problem
    ###     use move(src, dst) to move disks
    ### YOUR CODE HERE
    if n==1:
        move(src, dst)
        return
    Hanoi(n-1, src, tmp, dst)
    move(src, dst)
    Hanoi(n-1, tmp, dst, src)
    ### END YOUR CODE

def run():
    ### use your Hanoi() to see your outputs
    Hanoi(4, 2, 3, 1)

if __name__ == '__main__':
    args = sys.argv[1]
    if args == "run":
        run()
        for output in outputs:
            print("%d -> %d" % (output[0], output[1]))
    elif args == "test":
        test_Recursion.test_Tower_of_Hanoi()
    else:
        raise RuntimeError('invalid run mode')