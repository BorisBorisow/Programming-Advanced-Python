def avg(values):
    return sum(values) / len(values)

line = int(input())

students = {}

for _ in range(line):
    data = input().split()
    name, grade_string = data
    grade = float(grade_string)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    grades_formatted = " ".join(f'{grade:.2f}' for grade in grades)
    grades_avg = avg(grades)
    grades_avg_formatted = f"{grades_avg:.2f}"
    print(f"{name} -> {grades_formatted} (avg: {grades_avg_formatted})")