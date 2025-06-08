# Single Inheritance 
class stu_data:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class stu_marks(stu_data):  
    def __init__(self, name, roll_no, marks):
        stu_data.__init__(self, name, roll_no) 
        self.marks = marks

    def display(self):
        print(f"Name of the student: {self.name}")
        print(f"Roll number: {self.roll_no}")
        print(f"Marks: {self.marks}")

student = stu_marks("Piyush", 101, 95)
student.display()
