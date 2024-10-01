# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:05:40 2024

@author: Ion
"""
import json
import os
from  datetime import datetime
import pandas as pd


cwd = os.getcwd()
Recipes = 'Recipes'
path = os.path.join(os.getcwd(),Recipes)

def get_all_ingredients(ricette,debug_ricette = [],debug = 0):
    tutti_gli_ingredienti = {}
    for indice_ricetta in [i for i in range(len(ricette))]:
        que = ricette[indice_ricetta]['ingredients']
        questi = [i[0].lower() for i in que]
        for q in questi:
            #if q == 'guanciale':
            #    print('mmmm.... guanciale')
            #    debug_ricette.append(indice_ricetta)
            if q not in tutti_gli_ingredienti:
                tutti_gli_ingredienti[q] = 1
            else:
                tutti_gli_ingredienti[q] +=1 
    return tutti_gli_ingredienti,debug_ricette 

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(os.path.join(os.getcwd(), Recipes), f))]

start = datetime.now()
print(f'{start} reading')
ricette = [json.loads(open(  os.path.join(path,i) ,'r',encoding='utf8').read()) for i in onlyfiles]
end = datetime.now()
print(f'{end} done')
print(f' it took {(end-start).seconds}')

ingredienti = 'sale , Zucchero , acqua, uovo'

ingredienti = [i.strip().lower() for i in ingredienti.split(',')]

ricette_pd = pd.DataFrame(data = ricette, columns = [i for i in ricette[0]])
debug_ricette = []
tutti_gli_ingredienti , debug_ricette  = get_all_ingredients(ricette,debug_ricette)

lista_general = []
count = 0
elem = {}
for x in ingredienti : 
    lista_this = []
    for indice_ricetta in [i for i in range(len(ricette))]:
        que = ricette[indice_ricetta]['ingredients']
        questi = [i[0].lower() for i in que]
        stringa = ''
        for i in questi:
            stringa += i + ' '
        if x in stringa:
            lista_this.append(indice_ricetta)
    print(f'for {x} found {len(lista_this)} recipes')
    lista_general.append(lista_this)
    elem[count] = x
    count+=1





from itertools import combinations

def find_common_combinations(lists):
    # Convert all lists to sets
    sets = [set(lst) for lst in lists]
    
    # Generate all possible combinations of the sets
    all_combinations = []
    for r in range(2, len(sets) + 1):
        all_combinations.extend(combinations(enumerate(sets), r))
    
    # Filter combinations to find those with common elements
    common_combinations = {}
    for comb in all_combinations:
        indices, sets_comb = zip(*comb)
        common_elements = set.intersection(*sets_comb)
        if common_elements:
            common_combinations[indices] = list(common_elements)
    
    return common_combinations


common_combinations = find_common_combinations(lista_general)

for comb, common in common_combinations.items():
    print(f"Combination: {comb}, Common elements: {common}")


