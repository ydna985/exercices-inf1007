#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import copy
import itertools


def get_maximums(numbers):
	return [max(x) for x in numbers]

def join_integers(numbers):
	return int("".join(str(x) for x in numbers))

def generate_prime_numbers(limit):
	premiers=[]
	nombre=[x for x in range(2,limit+1)]
	while len(nombre)!= 0:
		premiers.append(nombre[0])
		nombre=[x for x in nombre if x%nombre[0] != 0]
	return premiers

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	answer=[]
	for letter in strings:
		for number in range(1,num_combinations+1):
			if excluded_multiples != None:
				if number%excluded_multiples==0:
					continue
			answer.append(letter+str(number))
	return sorted(answer, key=lambda letter_number: letter_number[1])

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
