__author__ = 'cuijianing'
def binaryAdd(a,b,c):
    x=0
    a.reverse()
    b.reverse()
    for i in range(0,len(a)):
        t=a[i]+b[i]+x
        (x,y)=divmod(t,2)
        c[i]=y
        c[i+1]=x
    return c.reverse()

if __name__ == '__main__':
    a=[1,1,1]
    b=[1,1,0]
    c=a[:]
    c.append(0)
    binaryAdd(a,b,c)
    print c