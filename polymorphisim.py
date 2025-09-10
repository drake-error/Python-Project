class animal():
    def sound(self):
        print("Animal make sound")

class dog(animal):
    def sound(self):
        print("Dog Barks")

class bird(animal):
    def sound(self):
        print("bird sing")

B1=bird()
B1.sound()
