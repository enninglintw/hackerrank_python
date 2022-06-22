m_length = input()
m = set(map(int, input().split()))
n_length = input()
n = set(map(int, input().split()))

union = m.union(n)
intersection = m.intersection(n)
symmetric_difference = union.difference(intersection)
symmetric_difference_ints = sorted(list(symmetric_difference))

for int in symmetric_difference_ints:
    print(int)
