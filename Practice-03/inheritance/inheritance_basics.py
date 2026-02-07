# Example 1: Simple parent class
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def print_name(self):
        print(self.firstname)


p = Person("John")
p.print_name()


# Example 2: Child class inheriting from parent
class Student(Person):
    pass

s = Student("Alice")
s.print_name()


# Example 3: Another child object
student2 = Student("Bob")
student2.print_name()


# Example 4: Parent method usage
person2 = Person("Emma")
person2.print_name()


# Example 5: Inheritance without extra methods
student3 = Student("Mike")
student3.print_name()
