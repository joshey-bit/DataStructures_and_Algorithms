# to sort the element and merge into single list
from merge import *
def merge_sort(a, left, right):
    #sort the slice a[left:right]
    if (right - left <= 1):
        return (a[left:right])
    elif (right - left)>1:
        mid = (left+right)//2
        L = merge_sort(a,left,mid)
        R = merge_sort(a,mid,right)

        return (merge(L,R))

a = list(range(0,100,2)) + list(range(1,100,2))
print(a)
print(merge_sort(a,0,len(a)))
