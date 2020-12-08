'''A program to convert decimal number to binary
eg. 242 to binary
this done by diviiding number by 2 and keeping the track of remainders
	number 	divn by 2(quotient) 	remainder
	242			121						0
	121			60						1
	60			30						0
	30			15						0
	15			7						1
	7			3						1
	3			1						1
	1			0						1
reading from bottom to up gives binary
'''

def base_2(decimal):
	#initialize an empty stack
	stack = []

	#to add remainder numbers to stack
	while decimal > 0:
		#add the remainder of number to stack
		remainder = decimal % 2
		stack.append(remainder)
		decimal = decimal // 2

	#read the binary stack as string
	bin_number = ''
	while stack != []:
		bin_number += str(stack.pop())

	return bin_number 


#test case
dec_number = 242
print(base_2(dec_number))


