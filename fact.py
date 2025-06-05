def fact(n):
     if (n==1 or n==0 ):
          return 1
     else:
          return (n*(fact(n-1)))
print("Enter the value of the number:-\n")
num= int(input())
factorial=fact(num)
print("The factorial of the number is :- \n",factorial)
