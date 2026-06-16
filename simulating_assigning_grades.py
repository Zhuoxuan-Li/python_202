import random

# Read the names from the provided file
with open("names_list.txt", mode="r") as file:
    names_text = file.read()

# Convert into a name list
names_list = names_text.split(",")

# Creat an empty dictionary for names and grades
names_and_grades = {}

# Assign a grade to each student
for name in names_list:
    clean_name = name.strip()
    grade = random.randint(50,100)
    names_and_grades[clean_name] = grade

# Creat a new file with all students' names and grades
with open("names_and_grades.txt",mode = "w") as file:
    for name,grade in names_and_grades.items():
        file.write(f"{name} received a grade of {grade}\n")

# Finad the top grade and the bottom grade
top_grade = max(names_and_grades.values())
bottom_grade = min(names_and_grades.values())

# Calculate the average grade
total_grade = 0

for grade in names_and_grades.values():
    total_grade += grade

average_grade = total_grade / len(names_and_grades)

# Print the student with the highest grade
for name,grade in names_and_grades.items():
    if grade == top_grade:
        print(f"The student with the top grade of {grade} is {name}")

# Print the student with the bottom grade
for name,grade in names_and_grades.items():
    if grade == bottom_grade:
        print(f"The student with the bottom grade of {grade} is {name}")

# Print the average grade with one-decimal precision
print(f"The average grade is {average_grade: .1f}")

