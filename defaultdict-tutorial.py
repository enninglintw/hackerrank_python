from collections import defaultdict

group_a_size, group_b_size = list(map(int, input().split(' ')))
group_a = [input() for i in range(group_a_size)]
group_b = [input() for i in range(group_b_size)]

word_index_tuples = [(word, i+1) for i, word in enumerate(group_a)]
word_indexes_dict = defaultdict(list)

for word, index in word_index_tuples:
    word_indexes_dict[word].append(index)

for word in group_b:
    indexes = word_indexes_dict.get(word, [-1])
    print(' '.join(list(map(str, indexes))))
