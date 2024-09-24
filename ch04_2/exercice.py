#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	names=name.split("-")
	firstname=names[0]
	firstname=firstname[0].upper()+firstname[1:].lower()
	return f"Bonjour, {firstname}"

def get_random_sentence(animals, adjectives, fruits):
	animal=animals[random.randrange(len(animals))]
	adjectif=adjectives[random.randrange(len(adjectives))]
	fruit=fruits[random.randrange(len(fruits))]
	return f"Aujourd’hui, j’ai vu un {animal} s’emparer d’un panier {adjectif} plein de {fruit}."

def format_date(year, month, day, hours, minutes, seconds):
	return f"{year:04}-{month:02}-{day:02} {hours:02}:{minutes:02}:{seconds:06.3f}"

def encrypt(text, shift):
	encrypted_msg=""
	text=text.upper()
	for letter in text:
		if ord(letter)>= 65 and ord(letter) <= 90:
			replacement=ord(letter)+shift
			if replacement > 90:
				replacement-=26
			elif replacement < 65:
				replacement+=26
			encrypted_msg+=chr(replacement)
		else:
			encrypted_msg+=letter
	return encrypted_msg

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
