# to sort a list of number in ascending order

def insertion_sort(li):
    for slice_end in range(len(li)):
        pos  = slice_end   # intiail position to be taken as end posn for sorted terms
        while pos > 0 and li[pos] < li[pos-1]:
            (li[pos],li[pos-1]) = (li[pos -1],li[pos])
            pos -= 1

li = list(range(5,0,-1))
insertion_sort(li)
print(li)