# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())

middle = N // 2
pattern = '.|.'
pattern_count = 1

for i in range(N):
    if i < middle:
        string = pattern * pattern_count
        pattern_count += 2
    elif i == middle:
        string = 'WELCOME'
        pattern_count -= 2
    else:
        string = pattern * pattern_count
        pattern_count -= 2

    print(string.center(M, '-'))
