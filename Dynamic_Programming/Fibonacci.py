# !/usr/bin/python
# Algorithms
# @Author: Kortez
# @Email: 595976736@qq.com

import sys
import test_Dynamic_Programming

def fast_Fibo(n):
    if n == 1:
        return 0, 1
    m = n // 2
    hprv, hcur = fast_Fibo(m)
    prev = hprv * hprv + hcur * hcur
    curr = hcur * (2 * hprv + hcur)
    next = prev + curr
    if n % 2 == 0:
        return prev, curr
    else:
        return curr, next

def Fibonacci(n):
    """ Solve Fibonacci problem.
        @params n (int): the input of the problem
        @returns the n-th fibonacci number
    """

    ### TODO - finish the function to compute the n-th fibonacci number
    ###     use move(src, dst) to move disks
    ### YOUR CODE HERE
    if n<=1:
        return 1

    # version 1: fastest
    _, ans = fast_Fibo(n+1)
    return ans

    ''' version 2: remember everything
    a = (n+1)*[0]
    a[0] = 1
    a[1] = 1
    for i in range (n-1):
        a[i+2]=a[i+1]+a[i]
    return a[-1]
    '''

    ''' version 3: simple recursion
    return Fibonacci(n-1) + Fibonacci(n-2)
    '''
    ### END YOUR CODE

def run():
    ### finish this function to see your outputs (optional)
    print(Fibonacci(4))
    return

if __name__ == '__main__':
    args = sys.argv[1]
    if args == "run":
        run()
    elif args == "test":
        test_Dynamic_Programming.test_Fibonacci()
    else:
        raise RuntimeError('invalid run mode')