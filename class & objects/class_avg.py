# Create student class that takes name & marks of 3 subjects as arguments in constructor. Create method to print average
class Student:
  def __init__(self, fullname, marks):
    self.name = fullname
    self.marks = marks
    
  def get_avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print(f"Hello {self.name}, your avg marks is: {sum/3}")
  
s1 = Student("Tony Stark", [91, 98, 87])
s1.get_avg()

s1.name = "Superman"
s1.get_avg()