__author__ = 'cuijianing'
import math

heapsize=0

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def parent(i):
    return math.ceil(i/2.0)

def swap(A,i,j):
    tmp=A[i]
    A[i]=A[j]
    A[j]=tmp

def MAX_HEAPIFY(A, i):
    global heapsize
    l=left(i)
    r=right(i)
    if l<heapsize and A[l]>A[i]:
        largest = l
    else:
        largest = i
    if r< heapsize and A[r]>A[largest]:
        largest = r
    if largest!=i:
        swap(A,i,largest)
        MAX_HEAPIFY(A,largest)

def BUILD_MAX_HEAP(A):
    for i in range(len(A)/2-1,-1,-1):
        MAX_HEAPIFY(A,i)

def HEAPSORT(A):
    global heapsize
    BUILD_MAX_HEAP(A)
    for i in range(len(A)-1,0,-1):
        swap(A,0,i)
        heapsize=heapsize-1
        MAX_HEAPIFY(A,0)

def HEAP_MAXIMUM(A):
    return A[0]

def HEAP_EXTRACT_MAX(A):
    global heapsize
    if heapsize<1:
        print 'heap underflow'
    max=A[0]
    A[0]=A[heapsize-1]
    heapsize=heapsize-1
    MAX_HEAPIFY(A,0)
    return max

def HEAP_INCREASE_KEY(A,i,key):
    if key<A[i]:
        print 'new key is smaller than current key'
    A[i]=key
    while i>0 and A[parent(i)]<A[i]:
        swap(A,i,parent(i))
        i=parent(i)

if __name__ == '__main__':
    A=[17,27,3,16,13,10,1,5,7,12,4,8,9,0]
    heapsize=len(A)
    HEAPSORT(A)
    print A
