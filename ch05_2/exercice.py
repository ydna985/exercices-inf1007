#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	price_sub_total=0
	for details in data:
		price_sub_total+=details[INDEX_PRICE]*details[INDEX_QUANTITY]
		taxe=price_sub_total*0.15
		total_price=taxe+price_sub_total
	resultat=f"SOUS TOTAL {price_sub_total:>6.2f}"
	resultat+=f"TAXES      {taxe:>6.2f}"
	resultat+=f"TOTAL      {total_price:>6.2f}"
	return resultat

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2


	return ""


def format_number(number, num_decimal_digits):
	
	while non_decimal_part != 0:
		chaine_partie_ent=(str(non_decimal_part%1000)*1000)+chaine_partie_ent
		non_decimal_part=0
	return chaine_partie_ent

def get_triangle(num_rows):
	top_border="+"*2
	for number in range(5):
		print()

	return top_border


if __name__ == "__main__":
	purchases = [
		("chaise ergonomique", 1, 399.99),
		("g-fuel", 69, 35.99),
		("blue screen", 2, 39.99)
	]
	print(format_bill_items(purchases).strip())
	print("- - - - - - - - - - - - - - - - - - -")
	print(format_bill_total(purchases).strip())

	print("\n------------------")

	print(format_number(-1420069.0678, 2))

	print("\n------------------")

	print(get_triangle(2))
	print(get_triangle(5))
