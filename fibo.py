__author__ = 'cuijianing'
def fibo(i):
    h1=(1+5**0.5)/2
    h2=(1-5**0.5)/2
    Fi=(h1**i-h2**i)/(5**0.5)
    return Fi
if __name__ == '__main__':
    i=float(raw_input('index of fibo is:'))
    Fi=fibo(i)
    print Fi