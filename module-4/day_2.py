# =======================================
# Loops
# =======================================

# While loop
num: int = 0
while num <= 10:
    print(num)
    num += 1

# get user password
# password: str = "12345678"
# input_password: str = input("Enter password: ")

# while input_password != password:
    # print("Incorrect password!")
    # print("Try again")
    # input_password: str = input("Enter password: ")

# print("Signin successfull")

MAX_PICKAXE_DAMAGE: dict = {
    "stone_pickaxe": 131,
    "iron_pickaxe": 250,
    "diamond_pickaxe": 1561,
}

pickaxe_damage = 131

while pickaxe_damage <= MAX_PICKAXE_DAMAGE["stone_pickaxe"]:
    print(pickaxe_damage)
    pickaxe_damage += 1

# For loop
nums: list = [1, 2, 3, 4, 5, 6, 7, 8]
for num in nums:
    print(num)

for num in range(10,0,-1): # range(start(default = 0), stop, step(default = 1))
    num = num * 2
    print(num)
