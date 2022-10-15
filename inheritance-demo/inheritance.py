class Marks:
    def __init__(self):
        self.m1 = int(input("Enter marks of C: "))
        self.m2 = int(input("Enter marks of Java: "))
        self.m3 = int(input("Enter marks of Python: "))

    def displaymarks(self):
        print("Marks of C: ", self.m1)
        print("Marks of Java: ", self.m2)
        print("Marks of Python: ", self.m3)


class Result(Marks): #Inheritance

    def __init__(self):
        Marks.__init__(self)
        self.total = self.m1 + self.m2 + self.m3
        self.percentage = self.total / 3

    def displayresult(self):
        print("Total: ", self.total)
        print("Percentage: ", self.percentage)

class Grade(Result): #Multi-level Inheritance
    def __init__(self):
        Result.__init__(self)
        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 80:
            self.grade = "B"
        elif self.percentage >= 70:
            self.grade = "C"
        elif self.percentage >= 60:
            self.grade = "D"
        else:
            self.grade = "F"

    def displaygrade(self):
        print("Grade: ", self.grade)


g = Grade()
g.displaymarks()
g.displayresult()
g.displaygrade()