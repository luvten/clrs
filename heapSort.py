__author__ = 'cuijianing'
import math

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def parent(i):
    return math.ceil(i/2.0)

def MAX_HEAPIFY(A, i):
    l=left(i)
    r=right(i)
    if l<len(A) and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r< len(A) and A[r]>A[largest]:
        largest = r
    if largest!=i:
        tmp=A[i]
        A[i]=A[largest]
        A[largest]=tmp
        MAX_HEAPIFY(A,largest)

def BUILD_MAX_HEAP(A):
    for i in range(len(A)/2-1,-1,-1):
        MAX_HEAPIFY(A,i)


if __name__ == '__main__':
    A=[17,27,3,16,13,10,1,5,7,12,4,8,9,0]
    BUILD_MAX_HEAP(A)
    print A
