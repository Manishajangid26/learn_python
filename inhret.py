class Person:
    def __init__(self , name):
        self.name = name

    def get_deteils(self ):
        return self.name  

class Student(Person):
    def __init__(self, name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def get_deteils_student(self):
        return self.roll_no

s = Student("manisha",26)
print(s.name)
print(s.roll_no)        
              