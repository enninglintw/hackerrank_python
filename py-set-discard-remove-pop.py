n = int(input())
s = set(map(int, input().split()))
commends_count = int(input())

for i in range(commends_count):
    command, *list = input().split(' ')
    value = int(list[0]) if list else None

    if command == 'remove':
        s.remove(value)
    elif command == 'discard':
        s.discard(value)
    elif command == 'pop':
        s.pop()

print(sum(s))
