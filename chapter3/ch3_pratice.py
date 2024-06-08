
def concat(a):
    head = a[0]
    tail = a[1:]
    if len(a) == 1:
        #BASE CASE
        return head 
    else:
        #RECURSIVE CASE
        return head+concat(tail)


def product(a):

    head = a[0]
    tail = a[1:]
    if len(a) == 1:
        #BASE CASE
        return head 
    else:
        #RECURSIVE CASE
        return head*product(tail)

test = ['hello',',','wes',' ', 'welcom home']
print(concat(test))

numTest = [2,3,4]
print(product(numTest))

# count Rooms added to ch3_floodfill.py


