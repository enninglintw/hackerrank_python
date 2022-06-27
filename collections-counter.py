shoes_count = int(input())
shoe_sizes = list(map(int, input().split(' ')))
customers_count = int(input())

sum = 0

for i in range(customers_count):
    shoe_size, price = list(map(int, input().split(' ')))

    if shoe_size in shoe_sizes:
        sum += price
        shoe_sizes.remove(shoe_size)

print(sum)
