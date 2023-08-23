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


class laptop:
    chargertype="C type"

    def __init__(self):
        self.price=34
        self.brand=""

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

hp=laptop()
hp.setprice(15000)
hp.getprice()