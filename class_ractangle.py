class Rectangle:
    def __init__(self,lang,width):
        self.l = lang
        self.w = width 
    def area(self):
        print(self.l*self.w)
r = Rectangle(5 , 5)
r.area()            
