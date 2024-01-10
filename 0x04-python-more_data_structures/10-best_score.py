#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    mx = list(a_dictionary.values())[0]
    key = list(a_dictionary.keys())[0]
    score = key
    for key, value in a_dictionary.items():
        if mx < value:
            score = key
    return score
