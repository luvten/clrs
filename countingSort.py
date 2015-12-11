__author__ = 'cuijianing'
from base import *
def COUNTING_SORT(A,B,k):
    C=[0]*(k+1)
    for j in range(0,len(A)):
        C[A[j]]=C[A[j]]+1
    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]
    print C
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1

if __name__ == '__main__':
    A=genarray(0,100,100)
    B=[0]*100
    COUNTING_SORT(A,B,100)
    print B