#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json

# TODO: Définissez vos fonction ici
def similarFile(first_file,second_file):
    first=open(first_file, "r", encoding="utf-8")
    second=open(second_file, "r", encoding="utf-8")
    similar=True
    line_fiff=0
    for index, line1 in enumerate(first):
        line2=second.readline()
        if line1 != line2:
            similar=False
            line_fiff=index+1
            break
    first.close()
    second.close()
    if similar == True:
        print("Ils sont identiques")
    else:
        print(f"Il y a une différence à la ligne {line_fiff}")
    return

def statsFile(name):
    my_dict={}
    with open(name, encoding="utf-8") as f:
        line=f.readline()
        while line != '':
            for word in line.split():
                if word in my_dict:
                    my_dict[word]+=1
                else:
                    my_dict[word]=1
            line=f.readline()
    print(my_dict)
    return

def translate_grade(grade, scaling):
    with open(grade, "r", encoding="utf8") as g, open(scaling, "r", encoding="utf8") as s, open("ch08_1/whatever.txt", "w", encoding="utf8") as yolo:
        data=json.load(s)
        for line in g:
            for key in data:
                if int(line)>= data[key][0] and int(line)<= data[key][1]:
                    yolo.write(line.strip() +":"+ key + "\n")
                    break

def more_space():
    int
    
if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")
    #similarFile("ch08_1/data/exemple.txt","ch08_1/data/exemple2.txt")
    #statsFile("ch08_1/data/exemple.txt")
    # TODO: Appelez vos fonctions ici, mettez vos fichiers de sortie dans le dossier "output".
    #translate_grade("ch08_1/data/notes.txt", "ch08_1/data/seuils.json")
    more_space()

