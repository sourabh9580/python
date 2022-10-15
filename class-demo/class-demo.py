# defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


A = Person("John", 30)
print(A)

# defining a class with a method


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def student_info(self):
        return f"{self.name} is {self.age} years old and is in {self.grade} grade"


B = Student("Jane", 20, "A")
print(B.student_info())

# comparing instances of a class
print(A == B)

# checking if an instance is an instance of a class
print(isinstance(A, Person))
