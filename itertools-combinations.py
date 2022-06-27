from itertools import combinations

input_1, input_2 = input().split(' ')
characters = sorted(input_1)
size = int(input_2)

for i in range(size):
    combination_tuples = list(combinations(characters, i+1))

    for combination_tuple in combination_tuples:
        print(''.join(combination_tuple))
