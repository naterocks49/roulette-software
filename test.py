from functions import find_equivalent, nonex_shared_eq,grab_spins
import json
from functools import reduce
'''
def nonex_shared_eq(dict):

    all_vals = []

    for i in dict:
        temp = []
        for j in dict[i]:
            temp.append(dict[i][j])
        all_vals.append(temp)

    print(all_vals)
    
    shared = list(reduce(lambda i, j: i & j, (set(x) for x in all_vals)))

    for i in shared:
        if i == "None":
            shared.remove(i)

    print(shared)
    
    return shared

with open('eq.json', 'r') as f:
    test_dict = json.load(f)
'''

grab_spins()