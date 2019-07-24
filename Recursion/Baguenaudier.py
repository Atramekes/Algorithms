# !/usr/bin/python
# Algorithms
# @Author: Kortez
# @Email: 595976736@qq.com

import sys
import test_Recursion

outputs = []

def flip(seq, func):
    """ Process a one-zero sequence seq according to func.
        @param seq (list[int]): the unprocessed sequence 
        @param func (int): to do which function
        @returns processed_seq (list[int]): the processed sequence 
    """
    ### TODO - calculate the processed_seq according to func
    ### YOUR CODE HERE (optional)
    processed_seq = seq.copy()
    if func == 0:
        processed_seq[-1] = 1 - seq[-1]
        index = 1
    else:
        n = 0
        for i in range(len(seq)-1, 0, -1):
            if seq[i] != 0:
                break
            n += 1
        if n + 2 <= len(seq):
            processed_seq[-n-2] = 1 - seq[-n-2]
            index = n + 2
    ### END YOUR CODE
    return processed_seq, index

def reversed_B(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    ans = []
    ans += reversed_B(n-1)
    ans += B(n-2)
    ans.append(1)
    ans += reversed_B(n-2)
    return ans

def B(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [1,0]
    seq = n*[1]
    ans = []
    ans += B(n-2)
    ans.append(1)
    ans += reversed_B(n-2)
    ans += B(n-1)
    return ans

def Baguenaudier(n):
    """ Solve Baguenaudier problem.
        @params n (int): dimension of the problem
        @returns solution (list[int]): the list of functions to solve the problem
    """

    ### TODO - finish the function to Baguenaudier Hanoi problem
    ### YOUR CODE HERE
    ans = B(n)
    s = n * [1]
    solution = []
    for i in ans:
        s, index = flip(s, i)
        solution.append(index)
    ### END YOUR CODE
    return solution

def run():
    ### finish this function to see your outputs (optional)
    ###     use flip() (optional)
    print(Baguenaudier(10))

if __name__ == '__main__':
    args = sys.argv[1]
    if args == "run":
        run()
    elif args == "test":
        test_Recursion.test_Baguenaudier()
    else:
        raise RuntimeError('invalid run mode')