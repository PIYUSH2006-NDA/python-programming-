class Person:
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ
        print("This is person information")
        
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Piyush", "Engineer")
a.info()
b = Person("Garvi", "Doctor")
b.info()
