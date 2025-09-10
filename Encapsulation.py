class company():
    def __init__(self):
        self._companyname="Google"

class A(company):
        pass

class accompany():
    def __init__(self):
        self.__companyname="Microsoft"
    def companyname(self):
        print(self.__companyname)


b1=A()
print(b1._companyname)

c1=accompany()
c1.companyname()

