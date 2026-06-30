from pathlib import Path

class Car:
    """Represent one car in the catalog"""

    def __init__(self, make, model, year):
        """Store the make, model, and year"""
        self.make = make.strip().title()
        self.model = model.strip().title()
        self.year = int(year)
    
    def __str__(self):
        """Give a formatted string for the car"""
        return f"{self.make} {self.model} - {self.year}"
    
    def __repr__(self):
        """Return a useful debug string for the car"""
        return (
            f"Car(make='{self.make}', "
            f"model='{self.model}', "
            f"year={self.year})"
        )

class CarCatalog:
    """Represent a catalog of cars"""

    def __init__(self, cars):
        """Store all cars in the catalog"""
        self.cars = cars
    
    def show_all_cars(self):
        """Print every car in the catalog"""
        for car in self.cars:
            print(car)

    def get_cars_by_make(self, make):
        """Create a list for the matching cars"""
        matching_cars = []

        # Format the make name
        make = make.strip().title()

        # Find all matching cars
        for car in self.cars:
            if car.make == make:
                matching_cars.append(car)
        
        return matching_cars

    def show_oldest_car(self):
        """Find the oldest year"""
        oldest_year = self.cars[0].year
        oldest_cars = []

        for car in self.cars:
            if car.year < oldest_year:
                oldest_year = car.year
        
        # Store all cars with the oldest year
        for car in self.cars:
            if car.year == oldest_year:
                oldest_cars.append(car)
        
        return oldest_cars

    def get_average_year(self):
        """Calculate the total of all years"""
        total_year = 0

        for car in self.cars:
            total_year += car.year
        
        # Calculate the average year
        average_year = total_year / len(self.cars)
        average_year = int(round(average_year, 0))

        return average_year


def load_cars(file_path):
    """Read the car data"""
    with open(file_path, mode="r") as file:
        lines = file.readlines()
    
    # Create an empty list for cars
    cars = []

    # Read each line and create a Car object
    for line in lines:
        line = line.strip()
        car_data = line.split(",")

        make = car_data[0]
        model = car_data[1]
        year = car_data[2]

        car = Car(make, model, year)
        cars.append(car)
    
    return cars

def show_menu():
    """Display the menu options"""
    print("")
    print("Choose a report:")
    print("1. View all cars sorted by make")
    print("2. Filter cars by make")
    print("3. Show the oldest car(s)")
    print("4. Show the average car year")
    print("5. Exit")


# Read the car data
file_path = Path.cwd() / "cars.csv"

# Load all cars before showing the menu
cars = load_cars(file_path)

# Create the car catalog
catalog = CarCatalog(cars)

# Show the menu until the user choose to exit
while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        catalog.show_all_cars()
    
    elif choice == "2":
        make = input("Enter a car make: ")

        matching_cars = catalog.get_cars_by_make(make)

        for car in matching_cars:
            print(car)
    
    elif choice == "3":
        oldest_cars = catalog.show_oldest_car()

        for car in oldest_cars:
            print(car)
    
    elif choice == "4":
        average_year = catalog.get_average_year()

        print(f"The average car year is {average_year}")
    
    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")