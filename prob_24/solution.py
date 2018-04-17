import math


def solution():
	values = [0,1,2,3,4,5,6,7,8,9]
	permutation = 1000000
	final = []
	while len(values)> 0:
		val_length = len(values)-1
		position = get_position(val_length,permutation)
		final.append(values[position])
		del values[position]
		permutation = get_left_over(position, val_length, permutation)
	print final


def get_position(length, left):
	position = left // math.factorial(length)
	if left % math.factorial(length) == 0:
		return position-1
	return position


def get_left_over(position, length, left):
	left_over = left - (position * math.factorial(length))
	return left_over
