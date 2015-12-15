__author__ = 'cuijianing'

from quicksort import RANDOMIZED_PARTITION
from base import *

import quicksort

def RANDOMIZED_SELECT(A, p, r, i):
    if p == r:
        return A[p]
    q = RANDOMIZED_PARTITION(A, p, r)
    k = q-p+1
    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A, p, q-1, i)
    else:
        return RANDOMIZED_SELECT(A, q+1, r, i-k)

if __name__ == '__main__':
    A=genarray(0, 100, 50)
    result = RANDOMIZED_SELECT(A, 0, 49, 1)
    quicksort.QUICKSORT(A, 0, 49)
    print result
    print A
