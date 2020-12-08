# to do insertion sort problem using recursive ideology
import sys
sys.setrecursionlimit(10000) #to set set recursion depth more than 1000

def rec_insertion(li):
    isort(li, len(li))

def isort(li,k):
    if k > 1:
        isort(li, k-1)
        insert(li, k-1)

def insert(li, k):
    pos  = k
    while pos > 0 and li[pos] < li[pos - 1]:
        (li[pos], li[pos-1]) = (li[pos - 1], li[pos])
        pos -= 1

li = list(range(5000, 0, -1))
li.sort()
print(li)
#rec_insertion(li)
