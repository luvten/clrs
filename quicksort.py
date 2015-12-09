__author__ = 'cuijianing'
from heapSort import swap
def QUICKSORT(A,p,r):
    if p<r:
        q=PARTITION(A,p,r)
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

if __name__ == '__main__':
    A=[5,4,2,1,3,0]
    QUICKSORT(A,0,len(A)-1)
    print A
