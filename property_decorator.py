class Student:
    def __init__(self, chem, phy, math):
        self.chem = chem
        self.phy = phy
        self.math = math
    
        
    @property # property decorator
    def percentage(self):
        return str((self.chem + self.phy + self.math) / 3) + "%"
    
        
stu1 = Student(94, 98, 78)        
print(stu1.percentage)

stu1.phy = 95
print(stu1.percentage)