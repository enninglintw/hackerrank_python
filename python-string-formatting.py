def print_formatted(number):
    width = len(format(number, 'b'))
    types = ['d', 'o', 'X', 'b']

    for i in range(1, number+1):
        values = ['{:>{width}{type}}'.format(i, width=width, type=type) for type in types]
        print(' '.join(values))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
