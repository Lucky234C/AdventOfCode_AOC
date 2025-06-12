# Advent Of Code 2024
# 2 December / Day 2: Red-Nosed Reports
# Part 1

safe_count = 0

def is_safe(report):
    intlist = list(map(int, report.split())) # List met allemaal INT
    
    for i in range(len(intlist) - 1):
        diff = abs(intlist[i] - intlist[i + 1]) # Verschil tussen 2 levels
        # abs neemt de aftand van een nummer tot 0 zowel + als -, hierdoor is de 'diff' altijd +, wat nodig is voor de volgende line 
        
        if diff < 1 or diff > 3: # kleiner 1 of groter dan 3 -> unsafe
            return False
        
    # Aflopend of oplopend
    is_increasing = all(intlist[i] < intlist[i + 1] for i in range(len(intlist) - 1))
    is_decreasing = all(intlist[i] > intlist[i + 1] for i in range(len(intlist) - 1))

    return is_increasing or is_decreasing
        


f = open("input.txt", "r")

for line in f:
    if is_safe(line):
        safe_count += 1

print(safe_count)
