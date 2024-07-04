

# local
from blessed import Terminal
from time import sleep 

def quicksort(items, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1 


    if right <= left:
        #BASE case 
        # only 0 or 1 element between right and left
        return

    # Start Partitions
    i = left                  # Start at the left end of the range
    pivotValue = items[right] # Select the last value as the pivot value

     # Iteration up to to not including the pivot
    for j in range(left, right):
        #if a value is less then the pivot, swap it to the left side of items
        if items[j] <= pivotValue:
            #swaw j with i and move I left by 1
            items[i], items[j] = items[j], items[i]
            i += 1
            printArray(items, i,j)

    # Put the pivot of the left side of items
    items[i], items[right] = items[j], items[i]
    
    quicksort(items, left, i-1)
    quicksort(items, i, right)




def printArray(a, pos, pos2):
    # Draw the Array 2 characters in from the edge
    x_offset = 2 
    y_offset = 2
    sleep(.2)
    
    with term.cbreak(), term.hidden_cursor():
        # clear the screen
        print(term.home + term.black_on_plum + term.clear)
    
        # draw !
        for y in range(len(a)):
            txt_erase = term.move_xy(x_offset, y+y_offset) + ' '
            txt_line = term.move_xy(x_offset, y+y_offset) + ''.join('='*a[y])
            if y == pos or y == pos2:
                print(term.grey_on_plum + txt_erase + txt_line, end='', flush=True)
            else:
                print(term.black_on_plum + txt_erase + txt_line, end='', flush=True)


term = Terminal()
a = [64, 31, 27, 1, 62, 13, 51, 3, 5, 6, 7, 14, 41, 55]
quicksort(a)
printArray(a, None, None)
