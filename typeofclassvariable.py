# ##instance mtd,cls mtd, ststic mtd 


# class laptop:
#     chargertype="C type"

#     def __init__(self):
#         self.price=34
#         self.brand=""

#     def setprice(self,price):
#         self.price=price

#     def getprice(self):
#         print(self.price)

# hp=laptop()
# hp.getprice()


# class laptop:
#     chargertype="C type"

#     def __init__(self):
#         self.price=34
#         self.brand=""

#     def setprice(self,price):
#         self.price=price

#     def getprice(self):
#         print(self.price)

# hp=laptop()
# hp.setprice(15000)
# hp.getprice()

# class laptop:
#     chargertype="C type"

#     def __init__(self):
#         self.price=34
#         self.brand=""

#     def setprice(self,price):
#         self.price=price

#     def getprice(self):
#         print(self.price)
    
#     @classmethod
#     def changechargertype(cls):
#         cls.chargertype="b type"
#         print("chargertype changed to B")
# hp=laptop()
# hp.setprice(15000)
# hp.getprice()
# laptop.changechargertype(laptop)



class laptop:
    chargertype="C type"

    def __init__(self):
        self.price=34
        self.brand=""

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
    
    @classmethod
    def changechargertype(cls):
        cls.chargertype="b type"
        print("chargertype changed to B")

    @staticmethod
    def info ():
        print("this is laptop class")


hp=laptop()
hp.setprice(15000)
hp.getprice()
hp.changechargertype(laptop)
hp.info()