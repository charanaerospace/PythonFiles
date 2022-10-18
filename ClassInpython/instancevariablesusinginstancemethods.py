class Student:
    def m1(self):
        self.a = 1
        self.b = 2
        self.c = 3
        print(self.a)
        print(self.b)
        print(self.c)
s= Student()
s.m1()
print(s.__dict__)        