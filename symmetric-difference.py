m_length = input()
m = set(map(int, input().split()))
n_length = input()
n = set(map(int, input().split()))

symmetric_difference_ints = sorted(list(m ^ n))

for int in symmetric_difference_ints:
    print(int)
