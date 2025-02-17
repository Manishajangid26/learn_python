#2. Write a Python class named Student with two attributes: student_id, student_name. Add a new 
# attribute: student_class. Create a function to display all attributes and their values in the 
# Student class.

class Student:
    def __init__(self,student_id,student_name ):
        self.student_id = student_id
        self.student_name = student_name



    def attribute(self):
        print("student id:",self.student_id)    
        print("student name:",self.student_name)    
        print("student class:",self.student_class)

    def set_student_class(self,student_class):
        self.student_class = student_class

Student = Student(26,"manisha")
print(Student.student_id)                