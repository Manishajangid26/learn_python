class Cicle:
    def circle_area(self,radius):
        return 3.14 * radius *radius

    def Cicle_parameter(self,radius):
        return 2 * 3.14 * radius

class Rectangle(Cicle):
    def rect_area(self,l,w):
        return l*w

    def rect_perameter(self,l,w):
        return 2 * l* w

a = Rectangle()
print(a.circle_area(4))
print(a.Cicle_parameter(4))
print(a.rect_area(4,6))
print(a.rect_perameter(4,6))            
