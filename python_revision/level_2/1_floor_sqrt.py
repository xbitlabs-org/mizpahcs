# Floor square root of a number

def floor_sqrt(number):
	if ( number == 0 or number ==1 ) :
		return number
	
	i = 1
	result = 1
	while result <= number:
		i += 1
		print('Value of : i : ', i)
		result = i*i

		print('Value of result : ', result)

	return i-1 # this loop will exit when the condition will be false, so we decrement i by 1

number = int(input('Enter a number to find floor sqrt of : '))

print(floor_sqrt(number))
