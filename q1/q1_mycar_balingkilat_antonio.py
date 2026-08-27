#Car Game
class Car:
    def __init__(self,brand,model,battery=33):        #Car Properties Function
        self.brand = brand
        self.model = model
        self.battery = battery
    def go(self,distance):                  #Battery Function
        self.battery -= distance / 25
        print("==============================")
        print("You travelled",distance,"km")
        print("Your",self.brand,self.model,"has",self.battery,"wH left.")
    def charge(self,wH):           #Charge Function
        self.battery += wH
        print("You successfully charged your car!")
        print("Your",self.brand,self.model,"has",self.battery,"wH left.")
        
brand = input("What is the brand of your electric car? ")
model = input("What is the model of your electric car? ")
eSasakyan = Car(brand,model)
while eSasakyan.battery > 0:
    prompt = input("What do you want to do? (go, charge) ").lower()
    if prompt == "go":
        distance = int(input("How far did you travel? "))
        eSasakyan.go(distance)
    elif prompt == "charge":
        wH = int(input("How much wH to charge? "))
        eSasakyan.charge(wH)
    else:
        print("!!!!Invalid Action!!!!")
print("")
print("=============================")
print("          GAME OVER")
print("=============================")
print("Your car ran out of battery..")
        
#eSasakyan.go(100)
#eSasakyan2 = Car("Tesla","Roadster",125)
#eSasakyan2.go(115)
