

# local
from blessed import Terminal
from time import sleep 

def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1 

    print('\nquicksort() called on this range ', items[left:right +1])
    print('............. The full list is:', items)

    if right <= left:
        #BASE case 
        # only 0 or 1 element between right and left
        return

    # Start Partitions
    i = left                  # Start at the left end of the range
    pivotValue = items[right] # Select the last value as the pivot value
    print('..................The pivot is:', pivotValue)

     # Iteration up to to not including the pivot
    for j in range(left, right):
        #if a value is less then the pivot, swap it to the left side of items
        if items[j] <= pivotValue:
            #swaw j with i and move I left by 1
            items[i], items[j] = items[j], items[i]
            i += 1

    # Put the pivot of the left side of items
    items[i], items[right] = items[j], items[i]
    
    print('....After swapping, the range is :' , items[left:right + 1])
    print('Recursivly Calling Quicksort on', items[left:i], ' and ', items[i+1:right +1])

    quicksort(items, left, i-1)
    quicksort(items, i, right)


a = [64, 31, 27, 1, 62, 13, 51, 3, 5, 6, 7, 14, 41, 55]
quicksort(a)
