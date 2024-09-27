#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text):
	counter=0
	for letter in text:
		if letter.isalnum() ==True:
			counter+=1
	return counter

def get_word_length_histogram(text):
	liste_mot=text.split()
	result=[0]
	for mot in liste_mot:
		lenght_word=get_num_letters(mot)
		if len(result)-1 < lenght_word:
			result=result+[0]*(lenght_word-(len(result)-1))
		result[lenght_word]+=1
	return result

def format_histogram(histogram):
	ROW_CHAR = "*"
	result=""
	for i in range(len(histogram)):
		if i == 0:
			continue
		result=result+f"{i:>2} {ROW_CHAR*histogram[i]}\n"

	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	result=""
	for i in range(max(histogram),0,-1):
		for x in range(len(histogram)):
			if x == 0:
				continue
			if histogram[x] >= i:
				result+=BLOCK_CHAR
			else:
				result+=" "
		result+="\n"	
	result+=LINE_CHAR*len(histogram)		

	return result


if __name__ == "__main__":
	word = "est?"
	print(f"The number of characters for '{word}' is: {get_num_letters(word)}")
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
