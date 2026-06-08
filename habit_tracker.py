# Build a Habit Tracker in Python, import module
import datetime

while True:

    # The information of user
    name = input("Enter your name:")
    name = name.title()

    # Ask for the starting date
    year = int(input("Enter the starting year:"))
    month = int(input("Enter the starting month:"))
    day = int(input("Enter the starting day:"))

    # Create a date 
    start_date = datetime.date(year, month, day)

    print(f"You entered as your starting date: {start_date}")

    # Ask how many days to track
    days_to_track = int(input("How many days are you tracking?"))

    # Ask for the habit
    habit = str(input(
        "What habit do you want to track?"
        "For example, study, exercise, etc.: "
    ))

    # Successful days
    successful_days = 0

    # Loop of each tracking day
    for day_number in range(1, days_to_track + 1):
        answer = input(
         f"Did you {habit} on day {day_number}?"
            "Answer 'yes' or 'no': "
        )

        if answer.lower() == "yes":
            successful_days = successful_days + 1


    # Calculate the ending date
    end_date = start_date + datetime.timedelta(days=days_to_track)

    # Calculate the success rate
    success_rate = (successful_days / days_to_track) * 100

    # Calculate how many days ago the tracking ended
    today = datetime.date.today()
    days_ago = (today - end_date).days

    # Display
    print("--------Summary--------")
    print(f"Habit tracker for {name}:")
    print(f"Habit:{habit}")
    print(f"Tracking period:{start_date} to {end_date}")
    print(f"Compeleted {successful_days} out of {days_to_track}.")
    print(f"Success rate: {success_rate:.2f}%")
    print(f"Your tracking is ended {days_ago} days ago.")

    # Ask if the user want to track again
    again = str(input(
        "Would you like to do another?"
        "Hit 'y' to continue or just hit Enter to quit: "
    ))

    if again.lower() != "y":
        break
