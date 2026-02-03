total_bill=float(input("Enter your total bill amount:"))
people=int(input("enter number of peoples:"))
share = total_bill / people
print(f"Total bill:{total_bill},Each person pays:{share}")
print(type(total_bill))
print(type(people))
print(type(share))