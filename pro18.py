print("Student Marks Manager")

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent List")

for name in students:
    print(name, ":", students[name])

total = sum(students.values())
avg = total / n

print("\nAverage Marks:", avg)

top = max(students, key=students.get)

print("Top Student:", top)