size_of_each_group = int(input())
room_numbers_list = list(map(int, input().split(' ')))
unique_room_numbers = set(room_numbers_list)

for unique_room_number in unique_room_numbers:
    room_numbers_list.remove(unique_room_number)

repeated_room_numbers = set(room_numbers_list)
captains_room_number = list(unique_room_numbers - repeated_room_numbers)[0]
print(captains_room_number)
