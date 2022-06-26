from itertools import permutations

input_1, *input_2 = input().split(' ')
characters = sorted(input_1)
size = int(input_2[0]) if input_2 else len(input_1)
permutation_tuples = list(permutations(characters, size))

for permutation_tuple in permutation_tuples:
    print(''.join(permutation_tuple))
