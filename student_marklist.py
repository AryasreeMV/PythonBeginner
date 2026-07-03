class Student:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
    
    def sum_marks(self):
        return self.m1+ self.m2+self.m3+self.m4+self.m5
    
    def avg_marks(self):
        return (self.sum_marks())/5
    
    def display(self):
        print(f"<-----Student Details----->")

        print(f"Name : {self.name}")

        print(f"Marks Obtained in each subjects : \nM1 = {self.m1} M2 = {self.m2} M3 = {self.m3} M4 = {self.m4} M5 = {self.m5}")

        print(f"Total Marks = {self.sum_marks()}")
        print(f"Average Mark = {self.avg_marks()}")


s1 = Student("Arya", 43, 45, 42, 41, 48)

s1.display()