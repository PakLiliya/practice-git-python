# Example 1: First parent class
class Person:
    def name(self):
        print("Person")


# Example 2: Second parent class
class Student:
    def role(self):
        print("Student")


# Example 3: Child inherits from two parents
class PersonStudent(Person, Student):
    pass


ps = PersonStudent()
ps.name()
ps.role()


# Example 4: Another object
ps2 = PersonStudent()
ps2.name()
ps2.role()


# Example 5: Reuse multiple inheritance
ps3 = PersonStudent()
ps3.name()
ps3.role()
