from collections import deque

'''
deque provides an O(1) time complexity for append and pop operations as 
compared to list which provides O(n) time complexity. so deque is prefered
'''

#using deque
stack = deque()

print("original stack: ")
print(str(stack))
print('\n')

#add/appending items in the end:
stack.append("a")
stack.append("b")
stack.append("c")
print("stack after adding items: ")
print(str(stack))
print('\n')

#popping the items from the stack in Last in first out manner
print("the items popped from the stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\n')

#stack after removing items
print(str(stack))

