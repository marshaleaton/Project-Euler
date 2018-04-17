def problem_23():
	potential_abundant = generate_list_options()
	potential_sum_of = list(potential_abundant)


	return


def get_abundant_numbers():
	abundant_numbers = []
	for i in range(1,28123):
		if is_number_abundant(i):
			abundant_numbers.append(i)
	print abundant_numbers
	print len(abundant_numbers)
	return abundant_numbers


def is_number_abundant(number):
	divisors = get_list_of_divisors(number)
	abundance = 0
	for i in divisors:
		abundance += i
	return abundance > number


def get_list_of_divisors(number):
	divisors = []
	for i in range(1, number-1):
		if number % i == 0:
			divisors.append(i)
	return divisors


def is_number_sum_of_abundance(number):
	return False


def generate_list_options():
	potential = []
	for i in (1, 28123):
		potential.append(i)
	return potential

