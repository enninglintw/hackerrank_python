test_cases_count = int(input())

for i in range(test_cases_count):
    set_a_len = int(input())
    set_a = set(map(int, input().split(' ')))
    set_b_len = int(input())
    set_b = set(map(int, input().split(' ')))

    is_set_a_a_subset_of_set_b = (set_a | set_b) == set_b
    print(is_set_a_a_subset_of_set_b)
