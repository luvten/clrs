__author__ = 'cuijianing'
import math
import random

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

def genarray(start,end,len):
    A=[0]*len
    for i in range(len):
        A[i]=random.randint(start,end)
    return A