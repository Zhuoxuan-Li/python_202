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
    grade = random.radiant(50,100)
    names_and_grades[clean_name] = grade

# Creat a new file with students' grade
with open("names_and_grades.txt",mode = "w") as file:
    for name,grade in names_and_grades.items():
        file.write(f"{name} received a grade of {grade}\n")

# The top grade and the bottom grade
top_grade = max(names_and_grades.values())
bottom_grade = min(names_and_grades.values())

# The average grade
total