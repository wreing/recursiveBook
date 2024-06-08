
def sumSeries(n):
    r = 0
    for x in range(1,n+1):
        r = r+x

    return r

def sumSeriesRecursive(n):
    if n == 1:
        return 1

    return n + sumSeriesRecursive(n-1)

def sumPowersOfTwo(n):
    r=0
    for x in range(1,n+1):
        r = r + 2**x
    return r

def sumPowersOfTwoRecursive(n):
    if n == 1:
        return 2**1
    return 2**n + sumPowersOfTwoRecursive(n-1)





#1  2  3  4  5
#1  3  6 10 15
print("Sum Series 5 : ", sumSeries(5))
print("Sum Series 5 : ", sumSeriesRecursive(5))


print("Sum Series 100 : ", sumSeries(100))
print("Sum Series 100 : ", sumSeriesRecursive(100))

#2  4  8  16  32
#2  6  14 30  62
print("Sum Pow2 5 : ", sumPowersOfTwo(5))
print("Sum Pow2 Rec 5 : ", sumPowersOfTwoRecursive(5))
