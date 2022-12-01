import operator
from itertools import islice
temp = open("input", "r").read().splitlines()

#part1
counter = 0
dict_results = {}
elf_counter = 0
for i in temp:
    if i != '':
        counter = counter + int(i)
    else:
        elf_counter = elf_counter + 1
        dict_results[elf_counter] = counter
        counter = 0

sorted_dict_descending = dict(sorted(dict_results.items(), key=operator.itemgetter(1),reverse=True))
print(f"Answer part1: {dict_results[list(islice(sorted_dict_descending, 1))[0]]}")

#part2
listing = list(islice(sorted_dict_descending, 3))
total_value_of_top_3 = 0
for key in listing:
    total_value_of_top_3 = total_value_of_top_3 + int(sorted_dict_descending[key])

print(f"Answer part2: {total_value_of_top_3}")
