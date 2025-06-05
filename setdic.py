#SET AND DICTIONARY METHODS
#SET
s1={1,2,3,5,4,6}
s2={3,5,6,4,9,8}
union1= print(s1.union(s2)) # union of s1,s2
(s1.update(s2)) 
print(s1,s2)
create= s1.symmetric_difference(s2)
print(create) # non common values
print(s1.issubset(s2)) # give boolean answer
print(s1.issuperset(s2))  # give boolean answer

#DICTIONARY
# Create an empty dictionary to store employee info
employees = {}

n = int(input("Enter the number of persons in the job: "))
for i in range(n):
    print(f"\nEnter details for person {i + 1}:")
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))

    employees[emp_id] = {
        "Name": name,
        "Salary": salary
    }

print("\nEmployee Information:")
for emp_id, info in employees.items():
    print(f"ID: {emp_id}, Name: {info['Name']}, Salary: {info['Salary']}")
