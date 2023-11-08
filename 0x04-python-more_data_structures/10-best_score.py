#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = 0
    best_sc_key = ""
    for key, val in a_dictionary.items():
        if val > max_val:
            max_val = val
            best_sc_key = key
    if best_sc_key in a_dictionary:
        return best_sc_key
    else:
        return None
