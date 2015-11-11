__author__ = 'cuijianing'
import random
def insertionSort(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while i >= 0 and key < a[i]:
            a[i+1]=a[i]
            a[i]=key
            i=i-1
        print a

def deInsertionhSort(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while i >=0 and key > a[i]:
            a[i+1]=a[i]
            a[i]=key
            i=i-1
        print a

def selectionSort(a):
    for i in range(0,len(a)-1):
        minValue=a[i]
        minIndex=i
        for j in range(i,len(a)):
            if minValue>a[j]:
                minValue=a[j]
                minIndex=j
        a[minIndex]=a[i]
        a[i]=minValue
        print a

def mergeSort(a,p,r):
    if p<r:
        q=(p+r)/2
        mergeSort(a,p,q)
        mergeSort(a,q+1,r)
        merge(a,p,q,r)

def merge(a,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*n1
    R=[0]*n2
    for i in range(0,n1):
        L[i]=a[p+i]
    for j in range(0,n2):
        R[j]=a[q+1+j]
    i=0
    j=0
    k=p
    while i<=n1-1 and j<=n2-1:
        if L[i]<R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1
    while i<=n1-1:
        a[k]=L[i]
        i+=1
        k+=1
    while j<=n2-1:
        a[k]=R[j]
        j+=1
        k+=1

if __name__ == '__main__':
    a=[]
    i=0
    while i<100:
        a.append(random.randint(0,100))
        i+=1
    #insertionSort(a)
    #deInsertionhSort(a)
    #selectionSort(a)
    mergeSort(a,0,len(a)-1)
    print a