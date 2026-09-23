class Sauce:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
        print("The sauce I prepared, which is the", self.name, "is ready! And it tastes..", self.taste, "!")

class TusokTusok:
    def __init__(self, name, sauce):
        self.name = name
        self.sauce = sauce
        print("My", self.name, "is being dipped by some tasty..", self.sauce.name, "!")
    def eat(self):
        print("I am currently eating a", self.name, "with some tasty", self.sauce.name, "!")
    def __del__(self):
        print("It looks like I threw the", self.name, "in the trash can, such a bummer..")
        
Vinegar = Sauce("vinegar", "sour")
Fishball = TusokTusok("Fishball", Vinegar)
Fishball.eat()

Fishball.sauce = None
