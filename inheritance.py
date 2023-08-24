# class dad():
#     def phone(self):
#         print("dad's phone")

# class mom():
#     def sweet (self):
#         print("mom's sweet")

# class son(dad,mom):
#     def laptop(self):
#         print("son's laptop")

# ram=son()
# ram.phone()
# ram.sweet()

### multiple level inheritance


# class grandfather():
#     def house(self):
#         print("grandfather's home")

# class appa(grandfather):
#     def car(self):
#         print("dad's car")

# class me (appa):
#     def laptop(self):
#         print("my laptop")

# thanu=me()
# thanu.laptop()
# thanu.car()
# thanu.house()        

##hirahey inheritance

# class amma():
#     def food(self):
#         print("amma's food")

# class son1(amma):
#     pass
# class son2(amma):
#     pass
# class son3(amma):
#     pass

# thanu=son1()
# thanu.food()


# hybrid inheritance
        


# ## super keyword

# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("i'm in class a")

# class b():
    
#     def display(self):
#         print("i'm in class b")

# ob1=a()
# print(a())

# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("i'm in class a")

# class b():
#     def __init__(self):
#         print("B")
#     def display(self):
#         print("i'm in class b")

# ob1=b()
# print(b())


# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("i'm in class a")

# class b(a):
#     def __init__(self):
#         print("B")
#     def display(self):
#         print("i'm in class b")

# ob1=b()

# class a():
#     def __init__(self):
#         print("A")
#     def display(self):
#         print("i'm in class a")

# class b(a):

#     def display(self):
#         print("i'm in class b")

# ob1=b()

class a():
    def __init__(self):
        print("A")
    def display(self):
        print("i'm in class a")

class b(a):
    
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("i'm in class b")

ob1=b()

