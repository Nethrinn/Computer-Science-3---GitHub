class Lab:
    def __init__(self, room_number):
        self.room_number = room_number

class Technician:
    def __init__(self, name):
        self.assigned_Lab = None
        self.name = name
    def assign_lab(self, lab_object):
        self.assigned_Lab = lab_object
        
    

chem_lab = Lab("302")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)

print(f"Technician {mr_cruz.name} is assigned to Room No. {mr_cruz.assigned_Lab.room_number}.")
