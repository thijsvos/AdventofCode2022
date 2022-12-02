#part1
D = {'X': 'A', 'Y': 'B', 'Z': 'C'}
W = {'X': 'C', 'Y': 'A', 'Z': 'B'}
L = {'X': 'B', 'Y': 'C', 'Z': 'A'}

with open('input', 'r') as f:
    strategy = f.readlines()

total_score = 0
for line in strategy:
    opponent, choice = line.split()
    total_score = total_score + ord(choice)-87
    if opponent == D[choice]:
        total_score = total_score + 3
    elif opponent == W[choice]:
        total_score = total_score + 6

print(total_score)
