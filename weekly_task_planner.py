# Ask the user to enter tasks separated by commas
task_input = input("Enter your tasks (comma separated): ")

# Convert the user's task string into a list
task_list = task_input.split(",")

print("")

# Create an empty list for cleaned tasks
clean_tasks = []

# Clean each task
for task in task_list:
    clean_task = task.strip()
    clean_task = clean_task.title()
    clean_tasks.append(clean_task)

# Create a tuple for the days of the week
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

# Create an empty list to store the weekly plan
weekly_plan = []

# Ask the user to assign one task to each day
for day in days:
    chosen_task = input(f"Which task will you do on {day}? ")
    chosen_task_clean = chosen_task.strip().title()

    if chosen_task_clean in clean_tasks:
        weekly_plan.append((day, chosen_task_clean))
    else:
        print(
            f"\"{chosen_task_clean}\" is not a valid task. "
            "Assigned \"Free Day\" instead."
        )
        weekly_plan.append((day, "Free Day"))

# Print the weekly plan
print("")
print("Your Weekly Plan:")
print("")

for day, task in weekly_plan:
    print(f"{day:<10} -> {task}")

# Ask which task the user wants to count
print("")
task_to_count = input("Which task would you like to count? ")
task_to_count = task_to_count.strip().title()

# Create a list of the scheduled tasks
scheduled_tasks = []

for day, task in weekly_plan:
    scheduled_tasks.append(task)

# Count how many times the chosen task appears
task_count = scheduled_tasks.count(task_to_count)

# Print the task count
print("")
print(f"You scheduled \"{task_to_count}\" {task_count} time(s).")