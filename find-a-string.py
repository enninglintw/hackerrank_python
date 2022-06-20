def count_substring(string, sub_string):
    sub_string_indexes = [string.find(sub_string, i) for i in range(len(string))]
    unique_sub_string_indexes = list(set(sub_string_indexes))
    unique_sub_string_indexes.remove(-1)
    count = len(unique_sub_string_indexes)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
