from itertools import product

def build_list(string):
    ''' Turn a string with integers separated by space into a sorted list'''
    return sorted(list(map(int, string.split(' '))))

list_a = build_list(input())
list_b = build_list(input())
product_tuples = list(product(list_a, list_b))

for product_tuple in product_tuples:
    print(product_tuple, end=' ')
