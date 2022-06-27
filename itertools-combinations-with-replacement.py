from itertools import combinations_with_replacement

input_1, input_2 = input().split(' ')
characters = sorted(input_1)
size = int(input_2)
combination_tuples = list(combinations_with_replacement(characters, size))

for combination_tuple in combination_tuples:
    print(''.join(combination_tuple))
