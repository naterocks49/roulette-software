import json
import tkinter as tk
from functools import reduce

def pretty_output(dict):

    string = ""

    for num in dict:
        string += f"{num}:\n"
        for type in dict[num]:
            string += f"{type}: {dict[num][type]}\n"

    return string
            

def find_equivalent(numbers, type_dict, excluded_spins):

    print(excluded_spins)

    split_num = [num for num in numbers.split()]

    types = []
    for i in type_dict:
        if type_dict[i] == True:
            types.append(i)


    all_types = ["20","-20","10","-10","1","-1","LEFT","RIGHT","SPECIAL"]
    remove_types = list(set(all_types).symmetric_difference(set(types)))

    final_dict = {}

    with open('eq.json', 'r') as f:
        data = json.load(f)

    for num in split_num:
        final_dict[num] = data[num]

    
    for num in final_dict:
        for type in remove_types:
            del final_dict[num][type]

    new_final = {}

    for num in final_dict:
        new_final[num] = {}
        for val in final_dict[num]:
            
            
            if final_dict[num][val] not in excluded_spins:
                
                new_final[num][val] = final_dict[num][val]

    return new_final

def find_shared_eq(dict):

    all_vals = []

    for i in dict:
        temp = []
        for j in dict[i]:
            temp.append(dict[i][j])
        all_vals.append(temp)
    
    

    shared = list(reduce(lambda i, j: i & j, (set(x) for x in all_vals)))
    
    return shared

def grab_spins():

    with open('last_spins.json', 'r') as f:
        spins = json.load(f)

    spins_arr = []

    for i in spins:
        spins_arr.insert(0, spins[i])
    
    return spins_arr

def add_last_spin(val):
    with open('last_spins.json', 'r') as f:
        spins = json.load(f)

    spins[str(len(spins) + 1)] = val

    with open('last_spins.json', 'w') as f:
        json.dump(spins,f, indent=4)

def backspace_spin():
    with open('last_spins.json', 'r') as f:
        spins = json.load(f)

    del spins[str(len(spins))]

    with open('last_spins.json', 'w') as f:
        json.dump(spins, f, indent=4)

def clear_spins():
    empty = {}
    with open('last_spins.json', 'w') as f:
        json.dump(empty, f, indent=4)
