#!/usr/bin/python3

# Author: Eugene Gaitano

# Date: 26th May 2026

def calculate_rental_cost(car_rented: str, days_rented: int) -> float:
    car_rented = car_rented.lower()

    total_cost: float = cars[car_rented] * days_rented
    print(f"Car rented: {car_rented}")
    print(f"Daily charge: {cars[car_rented]}")
    print(f"Days rented: {days_rented}")
    print(f"Total cost: {total_cost:.2f}")

    return total_cost

cars: dict[str, float] = {
    "toyota vitz": 1000.00,
    "range rover vogue": 3500.00,
}

for car in cars:
    print(car)

car_rented: str = input("Which car do you want to rent? ")

# if car_rented in cars:
    # days_rented: int = int(input("How many days would you like to rent? "))
    # calculate_rental_cost(car_rented, days_rented)
# else:
    # print("Oops! Car not found")


while car_rented.lower() not in cars:
    print("Oops! Car not found")
    print("Pick another car\n")
    car_rented: str = input("Which car do you want to rent? ")

days_rented: int = int(input(f"How many days would you like to rent the {car_rented}? "))
calculate_rental_cost(car_rented, days_rented)
