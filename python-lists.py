if __name__ == '__main__':
    N = int(input())
    list = []

    for i in range(N):
        command, *numbers = input().split(" ")

        if command == "insert":
            position = int(numbers[0])
            integer = int(numbers[1])
            list.insert(position, integer)
        elif command == "print":
            print(list)
        elif command == "remove":
            integer = int(numbers[0])
            list.remove(integer)
        elif command == "append":
            integer = int(numbers[0])
            list.append(integer)
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
