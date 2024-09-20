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
	decimal_part=abs(number) % 1
	non_decimal_part=int(abs(number))
	nbr_restant=0
	chaine_partie_ent=""
	while nbr_restant >= 1000:
		nbr_restant=number%1000
		chaine_partie_ent=str(nbr_restant)+chaine_partie_ent
		
	for nb in non_decimal_part:
		if counter % 3 == 0 and counter != 0 and counter != len(nb):
			result+=" "
		result+=nb
		counter+=1
	counter=0
	result+="."
	for nb in decimal_part:
		if counter % 3 == 0 and counter != 0 and counter != len(nb):
			result+=" "
		result+=nb
		counter+=1
	return result

def get_triangle(num_rows):
	return ""


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
