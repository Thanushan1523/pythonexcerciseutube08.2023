# private variable

# class company ():
#     def __init__(self):
#         self.__companyname="Genious"

#     def companyname(self):
#         print(self.__companyname)

# c1=company()
# c1.companyname()

# protector
class company ():
    def __init__(self):
        self._companyname="Genious"

class b(company):
    pass

b1=b()
c1=company()
print(c1._companyname)