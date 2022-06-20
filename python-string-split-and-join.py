def split_and_join(line):
    words = line.split(" ")
    string = "-".join(words)
    return(string)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
