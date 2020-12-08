from linked_list import LinkedList

link_list = LinkedList()
link_list.insert_start(3)
link_list.insert_start(122)
link_list.insert_start(55)
link_list.insert_end(35)
link_list.list_traverse()
print('')
link_list.remove(122)
link_list.list_traverse()
print('')
link_list.insert_start(122)
link_list.list_traverse()

print('')
link_list.remove(35)
link_list.list_traverse()

print('')
print(f'the size of the list: {link_list.size1()}')