#A program to check whether the paranthesis are balanced
'''
eg. {[()]}({}) : Balanced
	}{][()]} : Un balanced
	{{} : unbalanced
	()) : Unbalanced
'''
from queue import LifoQueue

def is_match(p1, p2):
	#check for match:
	if p1 == '(' and p2 == ')':
		return True

	elif p1 == '[' and p2 == ']':
		return True

	elif p1 == '{' and p2 == '}':
		return True

	elif p1 == '<' and p2 == '>':
		return True

	else:
		return False


def is_paren_balanced(exprn):
	#initialize the stack
	stack = LifoQueue(maxsize= len(exprn))
	#set balanced flag to True:
	is_balanced = True
	#initailize the index to 0 and traverse upto length of the expression
	index = 0

	while index < len(exprn) and is_balanced:
		char = exprn[index]
		if char in ['(','[','{','<']:
			stack.put(char)
		else:
			# the starting character is closing parantheses therefore the stack is empty
			if stack.empty():
				is_balanced = False
			else:
				# pop the top/last item 
				top_character = stack.get()

				#check whether the top charcheter and the char is match:
				if not is_match(top_character, char):
					is_balanced = False
		index += 1

	#the parenthesis is balanced if stack is empty and is_balanced is true:
	if stack.empty() and is_balanced:
		return True
	else:
		return False




#chaeck:

exp = '(('

if is_paren_balanced(exp):
	print('Balanced')
else:
	print('Unbalanced')
