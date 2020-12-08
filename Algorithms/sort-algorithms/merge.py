# to merge two sorted list

def merge(A, B):
    (c, m, n) = ([],len(A), len(B))
    (i,j) = (0,0) # i= index of list A, j is index of list B
    while i+j < m+n:
        if i == m: # A is empty
            c.append(B[j])
            j = j + 1
        elif j == n: # B is empty
            c.append(A[i])
            i = i + 1
        elif A[i] <= B[j]:
            c.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            c.append(B[j])
            j = j + 1
    return (c)

