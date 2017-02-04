def verify(x):
	result = 0
	if x[0] == 'a' or x[0] == 'b' or x[0] == 'c' or x[0] == 'd' or x[0] == 'e' or x[0] == 'f' or x[0] == 'g':
		result = result + 1
	for number in str(range(8)):
		if number == x[2]:
			result = result + 1
	if result == 2:
		return '+'
	else:
		return '-' 
def start():	
	coordinate_00 = raw_input('Please enter a cordinate (a-g,1-7)\n') 
	if verify(coordinate_00) == '-':
		print 'Error'
		start()
	else:
		return coordinate_00
def get_position(x):
	result = []
	dirc = raw_input('\nUp\nDown\nLeft\nRight\n\n')
	if dirc.lower() == 'up':
		if x[0] == 'a' or x[0] == 'b':
			print 'Error'
			get_position(x)
		else:
			result.append(x)
			result.append(up(x[0]) + x[1] + x[2])
			result.append(up(up(x[0])) + x[1] + x[2])
	elif dirc.lower() == 'down':
		if x[0] == 'f' or x[0] == 'g':
			print 'Error'
			get_position(x)
		else:
			result.append(x)
			result.append(down(x[0]) + x[1] + x[2])
			result.append(down(down(x[0])) + x[1] + x[2])
	elif dirc.lower() == 'left':
		if x[1] == '1' or x[1] == '2':
			print 'Error'
			get_position(x)
		else:
			result.append(x)
			result.append(x[0] + x[1] + left(x[2]))
			result.append(x[0] + x[1] + left(left(x[2])))
	elif dirc.lower() == 'right':
		if x[1] == '6' or x[1] == '7':
			print 'Error'
			get_position(x)
		else:
			result.append(x)
			result.append(x[0] + x[1] + right(x[2]))
			result.append(x[0] + x[1] + right(right(x[2])))
        return result

def up(x):
	if x == 'g':
		return 'f'
	elif x == 'f':
		return 'e'
	elif x == 'e':
		return 'd'
	elif x == 'd':
		return 'c'
	elif x == 'c':
		return 'b'
	elif x == 'b':
		return 'a'

def down(x):
	if x == 'a':
		return 'b'
	elif x == 'b':
		return 'c'	
	elif x == 'c':
		return 'd'
	elif x == 'd':
		return 'e'
	elif x == 'e':
		return 'f'
	elif x == 'f':
		return 'g'	

def left(x): 
	if x == '7':
		return '6'
	elif x == '6':
		return '5'
	elif x == '5':
		return '4'
	elif x == '4':
		return '3'
	elif x == '3':
		return '2'
	elif x == '2':
		return '1'

def right(x):
	if x == '1':
		return '2'
	elif x == '2':
		return '3'
	elif x == '3':
		return '4'
	elif x == '4':
		return '5'
	elif x == '5':
		return '6'
	elif x == '6':
		return '7'

def p1_turn():
        start_number = len(p2_position)
	print '\nPlayer 1:\n'
	guess = raw_input('Fire coordinates:\n')
	if verify(guess) == '-':
		print 'Error'
		p1_turn()
        else:
	        for item in p2_position:
		        if guess == item:
			        p2_position.remove(guess)
			        if len(p2_position) == 0:
				        print 'YOU WIN!!!'
			        else:
				        print 'HIT'
				        p2_turn()
        end_number = len(p2_position)
        if end_number == start_number:
		print 'MISS'
		p2_turn()

def p2_turn():
        start_number = len(p1_position)
	print '\nPlayer 1:\n'
	guess = raw_input('Fire coordinates:\n')
	if verify(guess) == '-':
		print 'Error'
		p2_turn()
        else:
	        for item in p1_position:
		        if guess == item:
			        p1_position.remove(guess)
			        if len(p1_position) == 0:
				        print 'YOU WIN!!!'
			        else:
				        print 'HIT'
				        p1_turn()
        end_number = len(p1_position)
        if end_number == start_number:
		print 'MISS'
		p1_turn

print '\nPlayer 1:\n'

p1_position = get_position(start())
print p1_position

print '\nPlayer 2:\n'

p2_position = get_position(start())
print p2_position

p1_turn()
