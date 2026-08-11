def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)

#O(n) — un solo ciclo simple, sin anidamiento.


def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

#O(n²) — dos ciclos anidados

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])

#O(1) El ciclo tiene un límite fijo (10), no depende del tamaño real de la entrada

def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

#O(n³)	Tres ciclos anidados