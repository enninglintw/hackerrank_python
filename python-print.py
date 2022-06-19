if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        print(i, end='')

# https://docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# `print(i, end='')` sets end as empty string '' instead of the default value '\n' in order to print all integers as a string without spaces.
