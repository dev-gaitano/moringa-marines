# =======================================
# Data structures
# =======================================

# Lists
# - Ordered
# - Mutable
# - Allows duplicates
fruits: list = ["orange", "mangoes", "nanasi"]

# Tuples 
# - Ordered
# - Immutable (Fater than a list)
# - Allows duplicates
cords: tuple = (56, 32)

# Sets
# - Unordered
# - Immutable
# - Doesn't allow duplicates
nums = set(1, 2, 3, 4, 5)

shopping_list = ["Eggs","Mangoes","Oranges","Mangoes","Beef","Mangoes","Avocadoes","Avocadoes"]
set_a = set(shopping_list)
set_b = set(["Apples","Mangoes","Eggs"])
set_c = set_a & set_b
print(set_c)
