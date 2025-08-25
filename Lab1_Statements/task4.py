miles_driven = (input("Please enter the amount of miles driven: "))
gallons_used = (input("Please enter the amount of gallons used: "))


while not miles_driven.isdigit():
    print("The amount of miles driven is not a number!")
    miles_driven = (input("Please enter the amount of miles driven: "))

while not gallons_used.isdigit():
    print("The amount of gallons used is not a number!")
    miles_driven = (input("Please enter the amount of gallons used: "))

miles_driven = float(miles_driven)
gallons_used = float(gallons_used)

print("Miles per gallon:", miles_driven/gallons_used)