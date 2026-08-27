class Hero:
    def __init__(self,name,health=100):
        self.name = name
        self.health = health
    def hurt(self,health):
        self.health = self.health - 10
        print("Morgana has 100 health left.")
        print("Arthur has",self.health,"health left.")

Arthur = Hero("Arthur",100)
Morgana = Hero("Morgana",100)
Arthur.hurt(10)
