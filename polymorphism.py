class Student():
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):           # Magic function of '+' operator
        return self.m1+other.m1, self.m2+other.m2
    
    def __sub__(self, other):           # Magic function of '-' operator
        return self.m1-other.m1, self.m2-other.m2


s1 = Student(9,6)
s2 = Student(10,7)

print(s1+s2)
print(s2-s1)