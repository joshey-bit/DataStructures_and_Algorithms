'''creating a Node with double reference class and double linked list class'''

class Node2():
	#creating node class and storing attributes
	def __init__(self, data):
		self.data = data
		self.next_node = None
		self.previous_node = None

#create a double linked list with suitable methods
class DoubleLinkedList():
	def __init__(self):
		self.head = None #head means the initial node in list, it is 'zero' here because the list is empty
		self.size = 0

	def insert_start(self,data):
		'''method to insert 'data' at begining'''
		self.size += 1
		new_node = Node2(data)

		if  not self.head: #if list is empty, not is used as not None evaluate to True, if condition is evaluated
			new_node.previous_node = None
			self.head = new_node 
		else:
			self.head.previous_node = new_node
			new_node.next_node = self.head 
			self.head = new_node
			new_node.previous_node = None 

	def list_traverse(self):
		actual_node = self.head

		while actual_node is not None:
			print(actual_node.data)
			actual_node = actual_node.next_node #new actual node is nextnode of old actual_node


li = DoubleLinkedList()
li.insert_start(3)
li.insert_start(4)
li.insert_start(5)
li.list_traverse()

