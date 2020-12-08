# the program for binary search algorithm
def bsearch(li, v, l, r):
    '''
    info = to check wheter v exists in li[l:r]
    '''
    if (r - l) == 0:
        return False
    mid = (l+r) // 2 # to check the mid point of sequnece
    if v == li[mid]:
        return True
    elif v < li[mid]:
        return (bsearch(li, v, l, mid))
    elif v > li[mid]:
        return (bsearch(li,v, mid+1, r))

check_list = list(range(101))
z = 67

print(bsearch(check_list,z, 0,101))
