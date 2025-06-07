class emp:
     def __init__(self,name,id):
          self.name=name
          self.id=id
     def showdetails(self):
          print(f"the name of the employee is {self.name} and id of the person is {self.id}")
e1=emp("piyush","36")
e1.showdetails()
