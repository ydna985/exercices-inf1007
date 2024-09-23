#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	orthogonal=False
	result=v1[0]*v2[0]+v1[1]*v2[1]
	if result == 0:
		orthogonal=True
	
	return orthogonal

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y
	x=point[0]-circle_center[0]
	y=point[1]-circle_center[1]
	lenght=math.sqrt(x**2+y**2)
	if(lenght > circle_radius):
		return False
	else:
		return True

def cash(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. Il faut remplir les variables twenties, tens, fives, ones, quarters, dimes et nickels avec le quantité de chaque dénomination.

	non_decimal_value=int(value)
	twenties=non_decimal_value//20
	reste=non_decimal_value%20
	tens=reste//10
	reste%=10
	fives=reste//5
	reste%=5
	ones=reste
	
	decimal_value=value%1
	twentifive_cents=round(decimal_value//0.25)
	decimal_value%=0.25
	ten_cents=round(decimal_value//0.10)
	decimal_value%=0.10
	five_cents=round(decimal_value//0.05)

	return (twenties, tens, fives, ones, twentifive_cents, ten_cents, five_cents)

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		result+=digit_letters[abs_value%16]
		abs_value=abs_value//16
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result="-"+result
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-420, 16, "0123456789ABCDEF"))
