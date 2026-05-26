# =======================================
# Python commands, Operators and control flow statements
# =======================================

# Variable declaration and and data types
user: str = "Gaitano"
print(type(user))
print(user)

my_num: int = 1234
print(type(my_num))
print(my_num)

# Lists
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Output: "apple"
fruits.append("grape")
print(fruits)  # Output: ["apple", "banana", "orange", "grape"]

# tuples
point = (3, 4)
print(point[0])  # Output: 3
x, y = point  # Tuple unpacking
print(x)  # Output: 3
print(y)  # Output: 4

# dicts
person = {"name": "John", "age": 25, "city": "New York"}
print(person["name"])  # Output: "John"
person["age"] = 30
print(person)  # Output: {"name": "John", "age": 30, "city": "New York"}

# Operators and Control flow statements
age: int = 190
user_registered: bool = True

if age < 18:
    print("Too young?")
elif age < 170 and user_registered == True:
    print("Uko kadi?")
else:
    print("Can you even vote?")
