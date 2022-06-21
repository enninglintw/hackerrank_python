import string

def print_rangoli(size):
    unique_letters = string.ascii_lowercase[:size][::-1]
    height = size*2 - 1
    width = height*2 - 1

    for i in range(1, size*2):
        count = size - abs(size-i)
        indexes = [count - abs(count-i) for i in range(1, count*2)]
        letters = [unique_letters[i-1] for i in indexes]
        pattern = '-'.join(letters).center(width, '-')
        print(pattern)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
