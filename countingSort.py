__author__ = 'cuijianing'
from base import *
def COUNTING_SORT(A,B,k):
    C=[0]*k
    for i in range(0,k):
        C[i]=0
    for j in range(1,len(A)-1):
        C[A[j]]=C[A[j]]+1
    for i in range(0,k):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1,0,-1):
        B[C[A[j]]]=A[j]
        C[A[j]]=C[A[j]]-1

if __name__ == '__main__':
    A=genarray(0,100,100)
    B=[0]*100
    COUNTING_SORT(A,B,100)
    print B