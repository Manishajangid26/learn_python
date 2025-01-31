class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_deteils(self):
        return self.name , self.age

class Student(Person):
    def __init__(self,name,age,branch,year):
        super().__init__(name,age)
        self.branch = branch
        self.year = year

    def Student_deteils(self):
        return (self.name , self.age , self.branch , self.year)

class Teacher(Person):
    def __init__(self ,name,age,paper):
        super().__init__(name,age)
        self.paper = paper

    def Teacher_deteils(self):
        return self.name

p = Person("manisha",19)
s = Student("manisha",19,"CSE",2022)
t = Teacher("vipin" , 25,"python")    

print(p.name)
print(s.name,s.age,s.branch,s.year)
print(t.name , t.age , t.paper)


           