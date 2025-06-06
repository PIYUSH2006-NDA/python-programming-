try:
    a = input("Enter the number:- \n")
    a = int(a)  
    print(f"The task of multiplication done on {a}")
    
    if a < 1:
        raise ValueError("Value should be more than 1")

    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")

except ValueError as e:
    print("Invalid number:", e)

finally:
    print("Welcome again")
