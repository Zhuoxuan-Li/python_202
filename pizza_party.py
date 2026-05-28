# Assist a pizza shop with orders for pizza parties

# Information of the user
name = str(input("What is your name?"))
people = int(input("How many of your guys are attending the party?"))

# The information about the pizza
slices_per_pizza = 8
slices_per_person = 3
pizza_costs = 12.50

# The name of the person
formatted_name = name.title()

# Calculation
total_slices = people * slices_per_person
total_pizza = total_slices // slices_per_pizza

# If the value of `total_pizza` is not an integer, round it up.
if total_slices % slices_per_pizza != 0:
    total_pizza = total_pizza + 1

total_costs = total_pizza * pizza_costs

# Result
print(f"Hello,{formatted_name}!")
print(f"Today is June 1, 2026")
print(f"The party will need {total_slices} slices of pizza.")
print(f"The party will need {total_pizza} pizzas.")
print(f"The total amount for the order is {total_costs:.2f} dollars.")