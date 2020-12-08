'''Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.'''
from array import *
def rotat(arr,d,n):
	for k in range(d):
		rotate_by_one(arr,n)
	return arr

def rotate_by_one(arr,n):
	temp = arr[0]
	for j in range(n-1):
		arr[j] = arr[j+1]
	arr[n-1] = temp

def print_array(arr,n):
	for i in range(n):
		print(arr[i], end=' ')


A = list(range(1,50001))
n = len(A)
rotat(A,2000,n)
print_array(A,n)





