# Many to many relationship
# Direct reference = store the related instances as a list
class Doctor:
    all_doctors = []

    def __init__(self, name) -> None:
        self.name = name
        self.patients = []
        Doctor.all_doctors.append(self)

    def __repr__(self) -> str:
        return self.name

    def treat_patient(self, patient):
        self.patients.append(patient)


class Patient:
    all_patients = []

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return self.name

    def doctors(self):
        return [doc for doc in Doctor.all_doctors if self in doc.patients]


doc1 = Doctor(name="Eugene")
doc2 = Doctor(name="Gaitano")

patient1 = Patient(name="Lilian", age=26)
patient2 = Patient(name="Pricilla", age=33)

doc1.treat_patient(patient1)
doc1.treat_patient(patient2)

print(doc1.patients)
print(patient1.doctors())


# Intermediary class/join table = A class is used to impose a relationship
# between two classes but with extra data
class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.cohort = None

    def enroll_in_class(self, tm):
        course_name = input("Enter course name: ")
        enrollment = Enrollment(self, tm, course_name)
        return enrollment


class Tm:
    def __init__(self, name) -> None:
        self.name = name
        self.cohort = None

    def __repr__(self) -> str:
        return self.name


class Enrollment:
    def __init__(self, student, tm, course_name) -> None:
        self.student = student
        self.tm = tm
        self.course_name = course_name


st1 = Student("Jonny")
tm1 = Tm("Mercy")

st1.enroll_in_class(tm1)
