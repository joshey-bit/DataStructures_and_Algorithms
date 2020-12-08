# Python program to  
# demonstrate stack implementation 
# using queue module

from queue import LifoQueue

stack = LifoQueue(maxsize= 3)  #specify the maximum size of the stack
print("initial stack size: " + str(stack.qsize()) +'\n')

#adding items to the stack
stack.put("a")
stack.put("b")
stack.put("c")

print("afteer adding items")
print("stack full: " + str(stack.full()))
print("stack size after adding items: " + str(stack.qsize()) +'\n')

#removing items from the stack:
print("the items removed in last in first out manner")
print(stack.get())
print(stack.get())
print(stack.get())
print('')

print("stack is empty: " + str(stack.empty()))

