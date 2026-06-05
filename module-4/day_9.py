# =======================================
# Object Oriented Programming (OOP) - Part 2
# =======================================

# Create a student class with atleast 5 attrs
# Ensure that one attr is a private mamber ad is acssessible via a property
# Add 2 methods: sign_in() and defer_class()

class Student:
    def __init__(self, firstname, lastname, age, course, gender, fee_balance,
                 signed_in=False) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.course = course
        self.gender = gender
        self.__fee_balance = fee_balance
        self.signed_in = signed_in

    @property
    def fee_balance(self):
        return self._fee_balance

    @fee_balance.setter
    def fee_balance(self, value):
        self._fee_balance = value

    def sign_in(self) -> str:
        if self.signed_in != True:
            self.signed_in = True
            return f"{self.firstname} {self.lastname} successfully signed in"
        else:
            return f"{self.firstname} {self.lastname} is already signed in"

    def defer_class(self) -> str:
        if self.course != None:
            self.course = None
            return f"{self.firstname} {self.lastname} has been successfully defered"
        else:
            return f"{self.firstname} {self.lastname} is already defered"

student1 = Student("Forest", "Nikolaus", 26, "SDFT17", "M", 0.00)

student1.fee_balance = 100000.00
print(student1.fee_balance)

print(student1.sign_in())
