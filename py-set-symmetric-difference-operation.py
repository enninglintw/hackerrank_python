n = int(input())
n_roll_numbers = set(input().split(' '))
b = int(input())
b_roll_numbers = set(input().split(' '))

symmetric_difference = n_roll_numbers ^ b_roll_numbers
print(len(symmetric_difference))
