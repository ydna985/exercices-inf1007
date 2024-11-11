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
	
	resultat=f"SOUS TOTAL {price_sub_total:>10.2f} $\n"
	resultat+=f"TAXES      {taxe:>10.2f} $\n"
	resultat+=f"TOTAL      {total_price:>10.2f} $"
	return resultat

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	result=""
	x=0
	for details in data:
		if len(details[0]) > x :
			x=len(details[0])
	
	for details in data:
		result+=f"{details[0]:<{x}} {details[2]*details[1]:>10} $\n"
	return result

def format_number(number, num_decimal_digits):
	decimals=abs(number)%1
	entier=str(int(number))
	chaine_partie_ent=""
	#chaine_partie_ent=(str((integer%1000)*1000))+chaine_partie_ent
	counter=0
	for i in range(-1,-(len(entier)+1),-1):
		chaine_partie_ent=entier[i]+ chaine_partie_ent
		counter+=1
		if counter == 3 and i != -len(entier) and entier[i-1] != "-":
			chaine_partie_ent=" "+chaine_partie_ent
			counter=0
	chaine_partie_ent=chaine_partie_ent+str(round(decimals,num_decimal_digits))[1:]
	
	return chaine_partie_ent

def get_triangle(num_rows):
	BORDERS="+"
	TRIANGLE="A"
	top_lower_border=BORDERS*(2*num_rows+1)
	result=""
	EMPTY=" "
	result+=top_lower_border
	for i in range(num_rows):
		result+=f"\n{BORDERS}{EMPTY*(num_rows-(1+i))}{TRIANGLE*(2*i+1)}{EMPTY*(num_rows-(1+i))}{BORDERS}"
	result+="\n"+top_lower_border
	return result


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
