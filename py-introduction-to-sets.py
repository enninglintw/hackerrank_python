def average(array):
    unique_numbers = list(set(array))
    return sum(unique_numbers) / len(unique_numbers)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
