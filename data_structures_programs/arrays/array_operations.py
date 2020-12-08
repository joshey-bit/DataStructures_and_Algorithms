import array

#create a new array of integer data type
arr1 = array.array('i',[1,2,3,4,5])
print('the new array created is: ', end='')
for i in range(0,5):
	print(arr1[i],end= ' ')
print('\r')	

#add new item to the end by append function
arr1.append(6)
print('the new array after appending is: ', end='')
for i in range(0,6):
	print(arr1[i],end= ' ')
print('\r')	

#insert a new item at index 2
arr1.insert(2,15) #(index, value)
print('the new array after inserting is: ', end='')
for i in range(0,7):
	print(arr1[i],end= ' ')
print('\r')	

#pop a value from index 5, return the popped value and the array after popping
print('the popped element: ', end='')
print(arr1.pop(5)) #arguement is the index of value
print('the new array after popping is: ', end='')
for i in range(len(arr1)):
	print(arr1[i],end= ' ')
print('\r')	

#remove 1st occurance of value and return the value, return the new array
#the remove method returns none, for arrays
print(arr1.remove(15))

print('the new array after removing is: ', end='')
for i in range(len(arr1)):
	print(arr1[i],end= ' ')
print('\r')

#get the index of a value from the array
print('the index of 4 is: ', end='')
print(arr1.index(4))
print('\r')

#reversethe array:
print(arr1.reverse()) #no arguemts is needed, and it returns none
print('the new array after reversing is: ', end='')
for i in range(len(arr1)):
	print(arr1[i],end= ' ')
print('\r')


#create new array for some other operations/function
arr = array.array('i',[1,2,3,4,5,4,5,1,5])
print('the array is: ',end='')
for i in range(len(arr)):
	print(arr[i],end= ' ')
print('\r')

#using typcode (note no parantheses as its an attribute) to find the datatype of array
print('the datatype of the array is: ',end='')
print(arr.typecode)
print('\r')

#using itemsize to check size of indiviual array item, doesnt count multiple occurance of same item
print('the itemsize of array is: ',end='')
print(arr.itemsize)
print('\r')

#using buffer_info() to return of address the array is stored in and no. of elements of array
print('the buffer info of the aaray is: ',end='')
print(arr.buffer_info())
print('\r')

#use count(item) to check number of occurance of item, ex: 5
print('the number of occurance of 5: ',end='')
print(arr.count(5))
print('\r')

#create a new array for extending purpose
arr2 = array.array('i',[15,16,17])

#use extend(array), to add new array to old array
arr.extend(arr2)

print('the array after extenstion is: ',end='')
for i in range(len(arr)):
	print(arr[i],end= ' ')
print('\r')

#use fromlist(list), method to add list items to array
li = [33,44,55] #a list

arr.fromlist(li)

print('the array after adding list is: ',end='')
for i in range(len(arr)):
	print(arr[i],end= ' ')
print('\r')

#use tolist() method to convert array into list

li2 = arr.tolist()

#print the list
print('the array converted to list: ',end='')
print(li2)





