
def sumArray(a):
    if len(a) == 0:
        return 0
    head = a[0]
    tail = a[1:]
    return head + sumArray(tail)


def rev(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    head = s[0]
    tail = s[1:]
    return rev(tail) + head 

def pal(s):
    if len(s) == 0 or len(s) == 1:
        return True 

    head = s[0]
    end  = s[-1]
    mid  = s[1:-1]

    return head == end and pal(mid)

def ittrPal(s):
    for i in range(0, len(s)):
        print("i = ", i)
        f = s[i]
        l = s[len(s)-1-i]:
        if i - len(s)-1-i == 0 or i - len(s)-1-i == 1:
            return True

        if s[i] != s[len(s)-1-i]:
            return False






a= [5,2,9,1]
print(sumArray(a))


s = 'abcd'
print(rev(s))

s = 'abcd'
print('Pal ', s, ' = ', pal(s))

s = 'abba'
print('Pal ', s, ' = ', pal(s))

s = 'abbba'
print('Pal ', s, ' = ', pal(s))

s = 'aa'
print('Pal ', s, ' = ', pal(s))

s = 'abba'
print('Itteritive')
print('Pal ', s, ' = ', ittrPal(s))

s = 'abcd'
print('Pal ', s, ' = ', ittrPal(s))

s = 'abba'
print('Pal ', s, ' = ', ittrPal(s))

s = 'abbba'
print('Pal ', s, ' = ', ittrPal(s))

s = 'aa'
print('Pal ', s, ' = ', ittrPal(s))



# Thoughs on Chapter 3
#3
