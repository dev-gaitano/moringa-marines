# =======================================
# Object Oriented Programming (OOP)
# =======================================

class Patient:
    def __init__(self, username: str, age: int, bill: float) -> None:
        self.username = username
        self.age = age
        self.bill = bill

    def discharge_patient(self) -> str:
        if self.bill == 0:
            return f"{self.username} has been discharged"
        else:
            return f"{self.username} has an outstanding amount: {self.bill}"

patient1 = Patient(username="Nicole Wambui", age=18, bill=5000.00)
patient2 = Patient(username="John Malebo", age=25, bill=5000.00)
patient3 = Patient(username="Auntie Madooh", age=37, bill=5000.00)

patients: list = [patient1, patient2, patient3]

for p in patients:
    print(f"{p.username} : {p.age}")

print(patient1.discharge_patient())
