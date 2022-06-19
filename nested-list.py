import math

if __name__ == '__main__':
    records = []
    grades = []

    for _ in range(int(input())):
        name = input()
        grade = float(input())
        records.append([name, grade])
        grades.append(grade)

    records = sorted(records)
    grades = sorted(list(set(grades)))
    second_lowest_grade = grades[1]

    for record in records:
        name, grade = record
        if math.isclose(grade, second_lowest_grade):
            print(name)
