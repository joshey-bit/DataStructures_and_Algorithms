# to sort without mergeing, and using partition method
#quick sort algorithm
import random

def quick_sort(A, l, r): # sort A[l:r]
    if r - l <= 1:
        return ()
    # start partitioning
    yellow = l + 1 # as A[l] is pivot, the left most element

    for green in range(l+1, r):
        if A[green] <= A[l]:
            (A[yellow],A[green]) = (A[green], A[yellow]) #replacing the elements
            yellow = yellow + 1

    # moving pivot to place
    (A[l],A[yellow-1]) = (A[yellow-1],A[l])

    quick_sort(A,l,yellow-1) #sort between l to yellow-1 as pivot is already sorted
    quick_sort(A,yellow, r) #sort between yellow to r as pivot is already sorted

#randomizing the list to increase efficiency of quick sort
def randomize(A):
    for i in range(0,len(A)//2):
        j = random.randrange(0,len(A),1)
        k = random.randrange(0,len(A),1)
        (A[j],A[k]) = (A[k],A[j])

A = list(range(500,0,-1))
# randomize(A)
# print(A)
# quick_sort(A,0,len(A))
# print(A)

k = int(input('enter the length of list: '))
lst = list(random.randrange(0,k))
print(lst)