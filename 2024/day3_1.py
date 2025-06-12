# Advent Of Code 2024
# 3 December / Day 3: Mull It Over
# Part 1

import re

with open("input.txt", "r") as f:
    mem = f.read()

# filterd al de coreecte mul instructies en slaat die op in een list genaamd "clean_mem"
clean_mem = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", mem)

f.close()

total = 0

# voor alle ints in clean_mem
for x, y in clean_mem:
    total += int(x) * int(y)

print(total)


