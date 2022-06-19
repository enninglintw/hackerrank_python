if __name__ == '__main__':
    n = int(input())
    name_marks_dict = {}

    for _ in range(n):
        name, *marks = input().split()
        marks = list(map(float, marks))
        name_marks_dict[name] = marks

    query_name = input()
    marks = name_marks_dict[query_name]
    averange_of_marks = sum(marks) / len(marks)
    formatted_averange_of_marks = format(averange_of_marks, ".2f")
    print(formatted_averange_of_marks)
