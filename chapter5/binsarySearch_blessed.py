
# local
from blessed import Terminal
from time import sleep 


def binarySearch(needle, haystack, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(haystack)-1



    if left > right:
        #BASECASE not in haystack
        return None

    mid = (left+right) // 2
    printArray(haystack, mid)
    if needle == haystack[mid]:
        return mid
    elif needle < haystack[mid]:
        return binarySearch(needle, haystack, left, mid-1)
    elif needle > haystack [mid]:
        return binarySearch(needle, haystack, mid+1, right)


def printArray(a, pos):
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
            if y == pos:
                print(term.grey_on_plum + txt_erase + txt_line, end='', flush=True)
            else:
                print(term.black_on_plum + txt_erase + txt_line, end='', flush=True)


term = Terminal()

with term.cbreak(), term.hidden_cursor():
    # I'd like to add a keyboard interupt to allow [q] to quit even if the maze isn't
    # solved but with the recuresive calls to print I'm not sure how to enable that
    a = [1,2,3,5,8,9,13,15,17, 19,19,21,22,23,25,27,31,37,39,41,43,44,47,47,50,51,53,59]
    x = binarySearch(37, a)
    if x == None:
        printArray(a, 0)
    else:
        printArray(a, x)


