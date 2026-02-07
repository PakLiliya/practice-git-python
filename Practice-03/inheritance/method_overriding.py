# Example 1: Parent method
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def welcome(self):
        print("Welcome", self.firstname)


# Example 2: Child overrides method
class Student(Person):
    def welcome(self):
        print("Hello student", self.firstname)


s = Student("Alice")
s.welcome()


# Example 3: Parent object
p = Person("John")
p.welcome()


# Example 4: Another overridden call
s2 = Student("Bob")
s2.welcome()


# Example 5: Parent still works
p2 = Person("Emma")
p2.welcome()
