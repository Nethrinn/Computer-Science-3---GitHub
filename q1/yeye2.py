class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
        def get_name(self):
            return self.name
        def get_bill_amount(self):
            return self.bill_amount
        def set_name(self, name):
            self.name = name
        def set_bill_amount(self, bill_amount):
            self.bill_amount = bill_amount
        def calculate_bill(self):
            print(f"Patient Name: {self.name}")
            print(f"Original Bill: {self.bill_amount}")
            print(f"Final Bill: {self.bill_amount}")

class Senior(Patient):
    def __init__(self, name, bill_amount):
            super().__init__(name, bill_amount)
            self.bill_final = self.bill_amount - self.bill_amount*0.20
    def calculate_bill(self):
            print(f"Patient Name: {self.name}")
            print(f"Original Bill: {self.bill_amount}")
            print(f"Final Bill: {self.bill_final}")

class Phil(Patient):
    def __init__(self, name, bill_amount):
            super().__init__(name, bill_amount)
            self.bill_final = self.bill_amount - self.bill_amount*0.15
    def calculate_bill(self):
            print(f"Patient Name: {self.name}")
            print(f"Original Bill: {self.bill_amount}")
            print(f"Final Bill: {self.bill_final}")


print("Hospital Billing System")
print("==============================")
regular_patient = Patient("Allen", 15000)
regular_patient.calculate_bill()
print("")
senior_patient = Patient("Joj", 15000)
senior_patient.calculate_bill()
print("")
philhealth_patient = Patient("Nito", 15000)
philhealth_patient.calculate_bill()
