set_a_len = int(input())
set_a = set(map(int, input().split(' ')))
other_sets_count = int(input())

for i in range(other_sets_count):
    operation, set_i_len = input().split(' ')
    set_i = set(map(int, input().split(' ')))

    if operation == 'update':
        set_a |= set_i
    elif operation == 'intersection_update':
        set_a &= set_i
    elif operation == 'difference_update':
        set_a -= set_i
    elif operation == 'symmetric_difference_update':
        set_a ^= set_i

print(sum(set_a))
