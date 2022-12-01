import operator

temp = open("input", "r").read().splitlines()
# print(temp)

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

# print(dict_results)
sorted_dict_descending = dict(sorted(dict_results.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_dict_descending)
