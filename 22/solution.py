def problem_22():
	name_file = open_file()
	names = convert_to_list(name_file)
	names = sort_names(names)
	score = iterate_names(names)
	print score
	return


def open_file():
	f = open('p022_names.txt', 'r')
	return f.read()


def convert_to_list(file_contents):
	names = file_contents.split(',')
	return names


def sort_names(names):
	names = sorted(names)
	return names


def iterate_names(sorted_names):
	location = 1
	sum_of_scores = 0
	for name in sorted_names:
		name = name.replace('"','')
		score = calculate_name_score(name, location)
		location += 1
		sum_of_scores += score
	return sum_of_scores

def calculate_name_score(name, location):
	score = 0
	for char in name:
		score += letter_score(char)
	return score * location


def letter_score(letter):
	letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
	           'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
	           'X': 24, 'Y': 25, 'Z': 26}

	return letters[letter]
