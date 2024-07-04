
def binarySearch(needle, haystack, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(haystack)-1

    print('Searching: ', haystack[left:right +1 ])

    if left > right:
        #BASECASE not in haystack
        return None

    mid = (left+right) // 2
    if needle == haystack[mid]:
        return mid
    elif needle < haystack[mid]:
        return binarySearch(needle, haystack, left, mid-1)
    elif needle > haystack [mid]:
        return binarySearch(needle, haystack, mid+1, right)






a = [1,2,3,8,13,19,19, 37]
print(binarySearch(13, a))
