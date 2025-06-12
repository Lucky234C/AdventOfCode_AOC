# Advent Of Code 2024
# 3 December / Day 3: Mull It Over
# Part 2

import re

do_sum = True #Wanneer False wordt alles voordat de eerste 'do_()' geweest is weg
total = 0

with open("input.txt", "r") as f:
    mem = f.read()

#  zoekt naar "do()", "don't()" en "mul()". en gaat dan over elke index/positie waar deze voorkomem.
for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):
    match x[0]:
        case 'do()':
            do_sum = True
        case 'don\'t()':
            do_sum = False
        case _:
            if do_sum:
                total += int(x[1]) * int(x[2])

print(total)
