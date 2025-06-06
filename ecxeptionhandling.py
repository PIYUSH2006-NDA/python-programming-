a= (input("Enter the number:- \n"))
print(f"The task of multiplication done on {a}")
try:
     for i in range(1,11):
          print(f"{a} x {i}={int(a)*i}")
except:
     print("invalid number please enter a valid number")
finally:
     print("welcome again")
     
