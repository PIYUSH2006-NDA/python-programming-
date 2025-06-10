#snake water gun game 
import random
import time
print("hello every one welcome to stone , paper , scissor ")
print("________________________________________________________________________________________________________________________")
def check(a,b):
     print(time.sleep(5))
     if(a==b):
          return "match tie"
          print("________________________________________________________________________________________________________________________")
     elif(a==1 and b==3):
          return  "player one win"
          print("________________________________________________________________________________________________________________________")
     elif(a==2 and b==3):
          return "player one win"
          print("________________________________________________________________________________________________________________________")
     elif (a==3 and b==2):
          return "player one win"
          print("________________________________________________________________________________________________________________________")
     else:
          return "player two win"
          print("________________________________________________________________________________________________________________________")

c=(input("\nPress 1 for 1-1 match with two players \nPress 2 for 1 player and another is computer \n________________________________________________________________________________________________________________________\n"))
match c:
     case "1":
          print(time.sleep(5))
          print("Select 1 out of 3 \n Press 1 for stone\n Press 2 for paper \n Press 3 for scissor\n")
          for round in range(1,4):
               print(f"round {round}\n________________________________________________________________________________________________________________________\n")
               p1=int(input("player one :- "))
               p2=int(input("player two :- "))
               result=check(p1,p2)
               print(result)
               print("________________________________________________________________________________________________________________________")
          if result == "player1":
                print("Player One wins this round")
                p1 += 1
          elif result == "player2":
                print("Player Two wins this round")
                p2 += 1
          else:
                print("This round is a tie")

                print("________________________________________________________________________________________________________________________")
          

     case "2":
          print(time.sleep(5))
          print("Select 1 out of 3 \n Press 1 for stone\n Press 2 for paper \n Press 3 for scissor\n")
          for round in range(1,4):
               print(f"round {round}\n")
               human=(input("player one :- "))
               comp=random.randint(1,3)
               print("computer entered value is :- ",comp)
               result=check(human,comp)
               print(result)
          if result == "player1":
                print("Player One wins this round")
                human += 1
          elif result == "player2":
                print("Player Two wins this round")
                comp += 1
          else:
                print("This round is a tie")
          
     



    
