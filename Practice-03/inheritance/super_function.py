# Example 1: Parent class
class Person:
    def __init__(self, fname):
        self.firstname = fname


# Example 2: Child using super()
class Student(Person):
    def __init__(self, fname):
        super().__init__(fname)


s1 = Student("Anna")
print(s1.firstname)


# Example 3: Adding new property
class Student2(Person):
    def __init__(self, fname, year):
        super().__init__(fname)
        self.graduation_year = year


s2 = Student2("Mark", 2025)
print(s2.firstname, s2.graduation_year)


# Example 4: Another object
s3 = Student2("Kate", 2024)
print(s3.firstname, s3.graduation_year)


# Example 5: super() reuse
s4 = Student2("Tom", 2026)
print(s4.firstname, s4.graduation_year)
