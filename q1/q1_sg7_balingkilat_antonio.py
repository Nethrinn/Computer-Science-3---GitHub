class Glassware:
    def __init__(self):
        print("Glassware is discovered")
        
class Beaker():
    def __init__(self):
        print("Beaker is created.")
                   
class Tray:
    def __init__(self):
        Glassware()
        print("")
        print("Tray is added.")
        self.indivBeakers = [Beaker() for i in range (5)]

        
    def __del__(self):
        del self.indivBeakers
        print("Tray has been deleted")
        for i in range (5):
            print("Beaker has been deleted")
  
equipment = Tray()
del equipment
