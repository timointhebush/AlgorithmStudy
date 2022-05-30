#!/bin/python3

import math
import os
import random
import re
import sys
import heapq as h

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    # Write your code here
    print(k)
    print(A)
    h.heapify(A)
    num = 0
    while len(A) != 0:
        if check(A, k):
            return num
        num += 1
        a = h.heappop(A)
        print("a", a)
        if len(A) == 0:
            break
        b = h.heappop(A)
        print("b", b)
        s = a + b * 2
        print("s", s)
        h.heappush(A, s)
    return -1


def check(A, k):
    for s in A:
        if s < k:
            return False
    return True


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + "\n")

    fptr.close()
