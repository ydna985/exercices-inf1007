#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def isvalid(chaine:str) -> bool:
    for letter in chaine:
        if letter != "a" and letter != "g" and letter != "c" and letter != "t":
            return False
    return True

def saisi():
    valid=False
    while valid == False:
        adn=input("Entrer la chaine adn: ")
        if isvalid(adn) == False:
            print("La chaine est incorrecte")
        else:
            valid=isvalid(adn)
    return adn

def proportion(adn:str, sequence:str):
    return adn.count(sequence)/len(adn)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    patern=input("que rechercher vous dans l'adn: ")
    print(proportion(saisi(), patern))
