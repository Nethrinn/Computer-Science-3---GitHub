class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_name(self, name):
        self.name = name
    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount
    def calculate_bill(self):
        print(f"Patient Name: {self.get_name}")
        print(f"Original Bill: ₱{self.get_bill_amount}")
        print(f"Final Bill: ₱{self.get_bill_amount}")

class Senior(Patient):
    def __init__(self, name, bill_amount):
            super().__init__(name, bill_amount)    
    def calculate_bill(self):
            first_bill = self.get_bill_amount()
            bill_final = first_bill - (bill_amount*0.20)
            print(f"Patient Name: {self.get_name}")
            print(f"Original Bill: ₱{self.get_bill_amount}")
            print(f"Final Bill: ₱{bill_final}")

class Phil(Patient):
    def __init__(self, name, bill_amount):
            super().__init__(name, bill_amount)
    def calculate_bill(self):
            second_bill = self.get_bill_amount()
            bill_final = second_bill - (second_bill*0.15)
            print(f"Patient Name: {self.get_name()}")
            print(f"Original Bill: ₱{self.get_bill_amount()}")
            print(f"Final Bill: ₱{bill_final}")


print("Hospital Billing System")
print("==============================")
regular_patient = Patient("Wan Dela Crews", 15000.00)
regular_patient.calculate_bill()
print("")
senior_patient = Senior("Mareya Santows", 15000.00)
senior_patient.calculate_bill()
print("")
philhealth_patient = Phil("Pedrow Rayes", 15000.00)
philhealth_patient.calculate_bill()
