'''creating a Node with single reference class and linked list class'''

class Node():
	#creating node class and storing attributes
	def __init__(self, data):
		self.data = data
		self.next_node = None

#create a linked list with suitable methods
class LinkedList():
	def __init__(self):
		self.head = None #head means the initial node in list, it is 'zero' here because the list is empty
		self.size = 0

	def insert_start(self,data):
		'''method to insert 'data' at begining'''
		self.size += 1
		new_node = Node(data)

		if  not self.head: #if list is empty, not is used as not None evaluate to True, if condition is evaluated
			self.head = new_node
		else:
			new_node.next_node = self.head 
			self.head = new_node 

	def size1(self):
		return self.size

	def size2(self):
		'''method to calculate size by traversing the list'''
		size = 0
		actual_node = self.head

		while actual_node is not None:
			size += 1
			actual_node = actual_node.next_node #new actual node is nextnode of old actual_node
		return size

	def insert_end(self,data):
		'''method to insert data to end'''
		self.size += 1
		actual_node = self.head
		new_node = Node(data)

		while actual_node.next_node is not None: #to check for last node in the list
			actual_node = actual_node.next_node
		actual_node.next_node = new_node

	def list_traverse(self):
		actual_node = self.head

		while actual_node is not None:
			print(actual_node.data)
			actual_node = actual_node.next_node #new actual node is nextnode of old actual_node

	def remove(self,data):
		if self.head is None:
			return()

		self.size = self.size - 1
		#start from beginning of list
		current_node = self.head #set current node as self.head
		previous_node = None

		while current_node.data != data:
			previous_node = current_node #new previous node is old current node
			current_node = current_node.next_node #new current node is next node of old current node

		if previous_node is None:
			self.head = current_node.next_node #head of list will be next node of current node, as current node 
			#will be removed
		else:
			previous_node.next_node = current_node.next_node #the next node of previous node will be the next node of current node
			#meaning current node will be removed







