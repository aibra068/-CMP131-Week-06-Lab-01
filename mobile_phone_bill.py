
# Student Name: Amaney Ibrahim
# Course Number: CMP 131
# Week Number: 6
# Lab Number: 01
# Assignment Title: Mobile Phone Service Bill
# Date: 10/08/26

# ~ Program Title ~

print()
print("==================================================")
print("           MOBILE PHONE SERVICE BILL")
print("==================================================")
print()

# ~ Part 1: ~ Display Available Packages ~

print("Available Mobile Phone Packages:")
print()
print("Package A:")
print("Monthly Charge: $39.99")
print("Included Minutes: 450")
print("Additional Minute Rate: $0.45")
print()
print("Package B:")
print("Monthly Charge: $59.99")
print("Included Minutes: 900")
print("Additional Minute Rate: $0.40")
print()
print("Package C:")
print("Monthly Charge: $69.99")
print("Included Minutes: Unlimited")
print("Additional Minute Rate: $0.00")
print()

# ~ Part 2: ~ User Input ~

package = input("Please select a package (A, B, or C): ").upper()
minutes_used = int(input("Please enter the number of minutes used: "))

# ~ Part 3: ~ Validate Package and Minutes ~

if package != "A" and package != "B" and package != "C":
    print("Error! Invalid package selection.")

elif minutes_used < 0:
    print("Error! Minutes used cannot be negative.")

# ~ Parts 4-6: Conditional Statements and Calculations ~
else:
    Additional_Minutes = 0
    Additional_Charge = 0

    if package == "A":
        Monthly_Charge = 39.99

        if minutes_used > 450:
            Additional_Minutes = minutes_used - 450
            Additional_Charge = Additional_Minutes * 0.45

    elif package == "B":
        Monthly_Charge = 59.99

        if minutes_used > 900:
            Additional_Minutes = minutes_used - 900
            Additional_Charge = Additional_Minutes * 0.40

    else:
        Monthly_Charge = 69.99

# ~ Calculate Total Monthly Bill ~

Total_Bill = Monthly_Charge + Additional_Charge

# ~ Part 7: Display Monthly Bill ~

print()
print("==================================================")
print("              MONTHLY PHONE BILL")
print("==================================================")
print(f"Selected Package: {package}")
print(f"Minutes Used: {minutes_used}")

if package == "C":
     print("Included Minutes: Unlimited")

print(f"Monthly Package Charge: ${Monthly_Charge:,.2f}")
print(f"Additional Minutes: {Additional_Minutes}")
print(f"Additional Minute Charge: ${Additional_Charge:,.2f}")
print("--------------------------------------------------")
print(f"Total Amount Due: ${Total_Bill:,.2f}")
print("==================================================")
