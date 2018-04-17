from decimal import *


def solution():
	setup_decimal()
	fractions = get_fractions()
	largest_cycle = {"size": 0, "denominator": 0}
	for fraction in fractions:
		cycle_size = find_cycle_size(fractions[fraction])
		if cycle_size > largest_cycle["size"]:
			largest_cycle["size"] = cycle_size
			largest_cycle["denominator"] = fraction
	print largest_cycle


def setup_decimal():
	getcontext().prec = 10000
	getcontext().rounding = ROUND_DOWN


def get_fractions():
	fractions = {}
	for number in range(1, 1000):
		fractions[str(number)] = str(Decimal(1)/Decimal(number))
	return fractions


def find_cycle_size(dec_number):
	dec_number = dec_number[2:]
	potential_pattern = ""
	# Flipping to work backwards since patterns can start at any point in decimal string
	flipped_number = dec_number[::-1]
	# Loop through until potential pattern repeats or gets too large
	for character in flipped_number:
		potential_pattern += character
		pattern_length = len(potential_pattern)
		# Check potential pattern to the next group to see if its repeating
		if potential_pattern == flipped_number[pattern_length:pattern_length*2]:
			return pattern_length
		if pattern_length > 5000:
			return 0
