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

# class Person():
#     def __init__(self,name):
#         self.name=name

# class Student (Person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade

#     def display(self):
#         print(self.name , self.grade)

# s1=Student("hi","A")
# print(s1.display())

# DOUBT
# class vehile():
#     def start():
#         print("vehile started")

# class car(vehile):
#     super() .__init__(start)

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary, department):
       super().__init__(name,salary)
       
       self.department=department
        
    def display(self):
        print(self.name,self.salary,self.department)

M1= manager("KAJAN","52","ACC")
M1.display()