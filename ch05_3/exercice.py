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
		if len(result) < len(mot):
			result=result+[0]*(len(mot)-len(result))
		result[len(mot)-1]+=1
	return result

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	word = "est?"
	print(f"The number of characters for '{word}' is: {get_num_letters(word)}")
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
