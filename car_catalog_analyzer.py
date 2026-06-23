from pathlib import Path

def load_cars():
    # Read the car data file
    file_path = Path.cwd() / "cars.csv"

    with open(file_path, mode = "r") as file:
        lines = file.readlines()
    
    # Creat an empty list to store car dictionaries
    cars = []
    
    # Clean each line and create a dictionary for each car
    for line in lines:
        line = line.strip()
        car_info = line.split(",")

        make = car_info[0].strip().title()
        model = car_info[1].strip().title()
        year = int(car_info[2].strip().title())

        car = {
            "make":make,
            "model":model,
            "year":year
        }
        cars.append(car)

    return cars

def show_all_cars():
    # Print all cars in dataset
    for car in cars:
        print(f"{car['make']} {car['model']} - {car['year']}")
              
def get_cars_by_make(make="toyota"):
    # Format make in title case
    make = make.strip().title()

    # Print all cars that match the selected make
    for car in cars:
        if car["make"] == make:
            print(f"{car['make']} {car['model']} - {car['year']}")

def show_oldest_cars():
    # Find the oldest year in the dataset
    oldest_year = cars[0]["year"]

    for car in cars:
        if car["year"] < oldest_year:
            oldest_year = car["year"]

    # Print all cars that match the oldest year
    for car in cars:
        if car["year"] == oldest_year:
            print(f"{car['make']} {car['model']} - {car['year']}")

def get_average_year():
    # Calculate the total of all car years
    total_year = 0

    for car in cars:
        total_year += car["year"]

    # Calculate the average year
    average_year = total_year / len(cars)
    average_year = int(round(average_year, 0))

    return f"The average car year is {average_year}"

# Load the car data before showing the menu
cars = load_cars()

# Show the menu until the user choose to exit
while True:
    print("")
    print("Choose a report:")
    print("1. View all cars sorted by make")
    print("2. Filter cars by make")
    print("3. Show the oldest car(s)")
    print("4. Show the average car year")
    print("5. Exit")

    choice = input("Enter your choice(Number Only):")

    if choice == "1":
        show_all_cars()

    elif choice == "2":
        make = input("Enter a car make: ")
        get_cars_by_make(make)

    elif choice == "3":
        show_oldest_cars()

    elif choice == "4":
        print(get_average_year())

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")