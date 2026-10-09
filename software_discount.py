# Student name: Amaney Ibrahim
# Course number: CMP-131
# Week number: 6
# Lab number: 01
# Assignment title: Assignment 6
# Date: 10/08/26
print()
print("=========================================================")
print("~   ~   ~   ~   ~ SOFTWARE DISCOUNT PROGRAM ~  ~  ~  ~  ~")
print("=========================================================")
print()

# ~ Part 1: Asking user for number of software units purchased ~

print()
print("          ~ User Input and Quantity Validation ~         ")
print()
quantity = int(input("Please Enter number of software units purchased: "))
if quantity <= 0: 
    print("Error! Quantity must be greater than 0")
else:
    Unit_Price = 99
    Original_Cost = quantity * Unit_Price

# ~ Part 2: Calculating Original Cost ~ 

Unit_Price = 99
Original_Cost = quantity * Unit_Price

# ~ Part 3: Determine Discount Rate ~

if quantity < 10: Discount_Rate = 0
elif quantity < 20: Discount_Rate = 0.20
elif quantity < 50: Discount_Rate = 0.30 
elif quantity < 100: Discount_Rate = 0.40 
else: 
    Discount_Rate = 0.50

# ~ Part 4: Calculate Discount Amount ~

Discount_Amount = Original_Cost * Discount_Rate

# ~ Part 5: Calculate Final Cost ~

Final_Cost = Original_Cost - Discount_Amount

# ~ Part 6: Display Purchase Report ~

print()
print()

print("========================================")
print("        SOFTWARE PURCHASE REPORT")
print("========================================")
print(f"Units Purchased: {quantity}")
print(f"Price Per Unit: ${Unit_Price:,.2f}")
print(f"Original Cost: ${Original_Cost:,.2f}")
print(f"Discount Percentage: {Discount_Rate:.0%}")
print(f"Discount Amount: ${Discount_Amount:,.2f}")
print(f"Final Purchase Cost: ${Final_Cost:,.2f}")
print("========================================")
