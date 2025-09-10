class phone():
    chargertype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Chargertype:",self.chargertype)

phone.chargertype="B-TYPE"

samsung=phone("Samsung","10000")
samsung.display()

Oneplus=phone("ONEPLUS","20000")
Oneplus.display()
