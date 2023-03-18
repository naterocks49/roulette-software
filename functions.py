import json
import tkinter as tk
from functools import reduce

def pretty_output(dict):

    string = ""

    for num in dict:
        string += f"{num}:\n"
        for type in dict[num]:
            string += f"{type}: {dict[num][type]}\n"
        string += "\n"

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

def ex_shared_eq(dict):

    all_vals = []

    for i in dict:
        temp = []
        for j in dict[i]:
            temp.append(dict[i][j])
        all_vals.append(temp)
    
    shared = list(reduce(lambda i, j: i & j, (set(x) for x in all_vals)))

    for i in shared:
        if i == "None":
            shared.remove(i)

    count = []
    for i in range(len(shared)):
        count.append(0)

    for ind, val in enumerate(shared):

        for idex, j in enumerate(all_vals):

            for t in all_vals[idex]:

                if val == t:

                    count[ind] += 1

    
    
    return shared, count

def nonex_shared_eq(dict):
    shared = []
    all_values = []

    for i in dict:
        temp = []
        for j in dict[i]:
            temp.append(dict[i][j])
        all_values.append(temp)

    all_vals = set()
    common_vals = set()

    for sub_arr in all_values:
        sub_arr_set = set(sub_arr)
        common_vals |= all_vals & sub_arr_set
        all_vals |= sub_arr_set

    for i in list(common_vals):

        if i != 'None':
            shared.append(i)

    count = []
    for i in range(len(shared)):
        count.append(0)

    for ind, val in enumerate(shared):

        for idex, j in enumerate(all_values):

            for t in all_values[idex]:

                if val == t:

                    count[ind] += 1

    return shared, count
            

def grab_spins():

    with open('last_spins.json', 'r') as f:
        spins = json.load(f)

    spins_arr = []

    for i in spins:
        spins_arr.insert(0, spins[i])

    return spins_arr

def clean_grab_spins(spins_arr):

    spins_str = ""

    for ind, val in enumerate(spins_arr):
        if ind == 0:
            spins_str += f"LAST SPIN: {val}\n"
        else:
            spins_str += f"{val}\n"
    
    return spins_str

def add_last_spin(val):
    with open('last_spins.json', 'r') as f:
        spins = json.load(f)

    vals_arr = [num for num in val.split()]
    count = len(vals_arr) + 1
    for i in vals_arr:
        spins[str(count)] = i

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

def filter_num_shared(shared, count, filter):

    final_shared = []
    final_count = []
    for ind, val in enumerate(shared):
        if count[ind] == filter:
            final_shared.append(val)
            final_count.append(count[ind])

    return final_shared, final_count


def pretty_eq(shared, count):

    textoutput = ""
    for ind, val in enumerate(shared):
        textoutput += f"Shared value: {str(val)} appears {str(count[ind])} time/s.\n"
    
    return textoutput
