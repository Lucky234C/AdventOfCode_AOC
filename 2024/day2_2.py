# Advent Of Code 2024
# 2 December / Day 2: Red-Nosed Reports
# Part 2

def check_diff_valid(levels): # bekijk of het verschil tussen 2 indexen lager dan 1 of hoger dan 3 is
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe(report):
    intlist = list(map(int, report.split()))
    
    if check_diff_valid(intlist) and (is_increasing(intlist) or is_decreasing(intlist)): #als er niets mis is hoer het report nu is
        return True
    
    for i in range(len(intlist)): # verwijder bij alle reports steeds een level
        new_list = intlist[:i] + intlist[i+1:]
        if check_diff_valid(new_list) and (is_increasing(new_list) or is_decreasing(new_list)): #alles juist nadat er 1 level verwijderd is? -> safe
            return True
    
    return False

def is_increasing(levels):
    return all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))

def is_decreasing(levels):
    return all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))


safe_count = 0

f = open("input.txt", "r")

for line in f:
    if is_safe(line.strip()): # strip() verwijderd de lege indexen (voor het geval dat deze aanweig zouden zijn)
        safe_count += 1

print(safe_count)
