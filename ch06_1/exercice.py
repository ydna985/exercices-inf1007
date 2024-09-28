#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values=[]
        while len(values) < 3:
            values.append(input("Enter une valeurs: "))
    values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        pass

    return False


def contains_doubles(items: list) -> bool:
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    answer_key=""
    best_grade=0
    for key,value in student_grades.items():
        if (sum(value)/len(value)) > best_grade:
            best_grade=(sum(value)/len(value))
            answer_key=key
    return {answer_key:best_grade}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dict={}
    for letter in sentence:
        dict[letter]=sentence.count(letter)
    sorted_key=sorted(dict, key=dict.__getitem__, reverse =True)
    for key in sorted_key:
        if dict[key] > 5:
            print(f"plus de 5 fois pour {key}")
    return dict


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
