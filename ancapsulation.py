class Person:
    def __init__(self,name,age):
        self.__name = name
        self.age = age

    def get_deteils(self):
        return self.name

class Student(Person):
    def __init__(self,name,age,branch,year):
        super().__init__(name,age)
        self.branch = branch
        self.year = year

    def get_deteils(self):
        return self.branch , self.year

s = Student("manisha",19,"cse",2022)                        
print(s._Person__name)