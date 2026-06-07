# Ask the Magic 8-Ball, import random module
import random

# Information of the user
name = str(input("What is your name?"))

# Enter nothing, Guest will be displayed
if not name:
    name = "Guest"
else: 
    name = name.title()

print(f"Welcome, {name}")

# Name length
name_length = len(name)

if name_length < 4:
    print("Your name is short and sweet!")
elif name_length > 6:
    print("Your name carries power in every letter!")
else:
    print("Great name! Balanced and bold.")

# Ask users a yes-or-no question
question = input("You can find out from me whether something is yes or no, so, what question would you like to ask now?\n>")

# Answer
answer = random.randint(1,5)

if answer == 1:
    response = "Yes, definitely."
elif answer == 2:
    response = "No, certainly not."
elif answer == 3:
    response = "Ask again later."
elif answer == 4:
    response = "Outlook not so good."
else:
    response = "It is possible."

# Display the response
print("MAGIC 8-BALL SAYS:")
print(f"{response}")