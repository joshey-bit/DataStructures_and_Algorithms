#A program to check whether the paranthesis are balanced
'''
eg. {[()]}({}) : Balanced
	}{][()]} : Un balanced
'''

def is_parenthesis_balanced(exprn):
	#initailize stack to store the data:
	stack = []
	for char in exprn:
		if char in ['(','[','{','<']:
			stack.append(char)
		else:
			#if the char is not the opening but closing, but with eg. }
			# } is not applicable so it means unblanced
			if stack == []:
				return False

			else:
				#start checking for balanced paranthesis
				current_char = stack.pop()
				if current_char == '(':
					if char != ')':
						return False

				if current_char == '[':
					if char != ']':
						return False

				if current_char == '{':
					if char != '}':
						return False

				if current_char == '<':
					if char != '>':
						return False
			

	#check for empty stack:
	if stack == []:
		return False

	#if none of the condition matched then the paranthesis are balanced
	return True

#Test the paranthesis:
expren = '['

if is_parenthesis_balanced(expren):
	print('Balanced')
else:
	print('Un-Balanced')

#this method has a problem refer another method
