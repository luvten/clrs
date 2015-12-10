__author__ = 'cuijianing'
from base import swap
import random
def QUICKSORT(A,p,r):
    if p<r:
        q=RANDOMIZED_PARTITION(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)

def PARTITION(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            swap(A,i,j)
    swap(A,i+1,r)
    return i+1

def RANDOMIZED_PARTITION(A,p,r):
    i=random.randint(p,r)
    swap(A,i,r)
    return PARTITION(A,p,r)

if __name__ == '__main__':
    A=[0]*100
    for i in range(100):
        A[i]=random.randint(1,100)
    QUICKSORT(A,0,len(A)-1)
    print A

