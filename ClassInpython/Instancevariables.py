# instance variables
# class Name
class Student:
    # attributes
    def __init__(self, name, id):
        self.name = name
        self.id   = id
s = Student('a', 1)
s1 = Student('b', 2)
print("Student Info")
print("Student name is", s.name)
print("id is", s.id)
print("Student name is", s1.name)
print("id is", s1.id)

       