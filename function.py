# def add():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     print(a+b)

# add()


# class laptop:
#     price=input("enter ram price:")
#     processor=""
#     ram=""

# hp= laptop()
# # hp.price=5000
# # hp.processor="i5"
# # hp.ram=input("enter ram capacity:")

# print("price is ",hp.price)



# class laptop():
#     def __init__(self):
#         self.ram=""
#         self.processor=""
#     def display (self):
#         print(self,"ram",self.ram)
#         print("processor",self.processor)
# # how to get the brand name of laptop when print
# hp=laptop()
# dell=laptop()
# hp.processor="i7"
# hp.ram="16gb"
# dell.processor="i5"
# dell.ram="8gb"

# hp.display()
# # dell.display()


class student():
    def __init__(self):
        self.name=""
        self.regnum=""
    def display (self):
        print("name",self.name)
        print("regesternumber",self.regnum)

stu1= student()
stu1.name= "ramanan"
stu1.regnum="64444"

stu1.display()

