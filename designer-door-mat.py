# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())

middle = N // 2
pattern = '.|.'
pattern_count = 1

for i in range(N):
    if i < middle:
        line_pattern = pattern * pattern_count
        pattern_count += 2
    elif i == middle:
        line_pattern = 'WELCOME'
        pattern_count -= 2
    else:
        line_pattern = pattern * pattern_count
        pattern_count -= 2

    print(line_pattern.center(M, '-'))
