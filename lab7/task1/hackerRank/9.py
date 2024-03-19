if __name__ == '__main__':
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])
    second_lowest_grade = None
    for i in range(1, n):
        if students[i][1] > students[0][1]:
            second_lowest_grade = students[i][1]
            break
    for student in students:
        if student[1] == second_lowest_grade:
            print(student[0])
