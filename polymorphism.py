# class Animal():
#     def sound(self):
#         print("animal makes sound")

# a1=Animal()
# a1.sound()
# print(a1.sound)

# class Dog(Animal):
#    def sound(self):
#     print("dog barkes") 

# a1=Animal()
# a1.sound()
# print(a1.sound)
# d1=Dog()
# d1.sound()
# print(d1.sound)

# class Shape ():
#     def area (self):
#         return 0
# s1=Shape()
# print(s1.area())
    
# class Rectangle(Shape):
#     def area (self):
#         return "area of the rectangle"
    
# r1=Rectangle()
# r1.area()
# print(r1.area())

class Person():
    def __init__(self,name):
        self.name=name

class Student (Person):
    def __init__(self,grade):
        self.grade=grade