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

# Operators and Control flow statements
age: int = 190
user_registered: bool = True

if age < 18:
    print("Too young?")
elif age < 170 and user_registered == True:
    print("Uko kadi?")
else:
    print("Can you even vote?")
