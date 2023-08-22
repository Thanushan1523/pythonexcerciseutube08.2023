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



class laptop():
    def __init__(self):
        self.ram=""
        self.processor=""
    def display (self):
        print("ram",self.ram)
        print("processor",self.processor)

hp=laptop()

hp.processor="i7"
hp.ram="i7"

hp.display()