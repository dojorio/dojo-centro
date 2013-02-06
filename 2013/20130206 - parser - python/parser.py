#-*- coding: utf-8 -*-




#[('N', '2'),('+', '+'),('N', '3'),('-', '-'),('N', '4')]
# 2 + 3 - 4
# 2
# (+, 2, 3)
# (-, (+, 2, 3), 4)

#[('N', '4'),('+', '+'),('N', '2'),('*', '*'),('N', '3')]
#4 + 2 * 3
#(+, parse(tokens[:+]), parse(tokens[+:]))

def parse(tokens):
	if len(tokens) == 1:
		return int(tokens[0][1])

	if ('+', '+') in tokens:
		op = ('+', '+')
	else:
		op = ('*', '*')

	op_index = (len(tokens)-1) - tokens[::-1].index(op)
	return (op[1], parse(tokens[:op_index]), parse(tokens[op_index+1:]))