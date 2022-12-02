#part1
D = {'X': 'A', 'Y': 'B', 'Z': 'C'}
W = {'X': 'C', 'Y': 'A', 'Z': 'B'}
L = {'X': 'B', 'Y': 'C', 'Z': 'A'}
PART2 = {'X': 0, 'Y': 3, 'Z': 6}
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

#part2
D = {'A': 1, 'B': 2, 'C': 3}
W = {'A': 2, 'B': 3, 'C': 1}
L = {'A': 3, 'B': 1, 'C': 2}
total_score = 0
for line in strategy:
    opponent, choice = line.split()
    total_score = total_score + PART2[choice]
    if choice == 'Y':
        total_score = total_score + D[opponent]
    elif choice == 'Z':
        total_score = total_score + W[opponent]
    elif choice == 'X':
        total_score = total_score + L[opponent]

print(total_score)
