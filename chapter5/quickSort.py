
def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1 

    print('\nquicksort() called on this range ', items[left:right +1])
    print('............. The full list is:', items)

    if right <= left:
        #BASE case 
        return

    # Start Partitions
    i = left
    pivotValue = items[right]
    print('..................The pivot is:', pivotValue)

    for j in range(left, right):
        #if a value is less then the pivot, swap it to the left side of items
        if items[j] <= pivotValue:
            items[i], items[j] = items[j], items[i]
