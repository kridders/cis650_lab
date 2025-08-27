miles_driven = input("Please enter the amount of miles driven: ")

while not miles_driven.isdigit():
    print("You did not enter a valid number for the amount of miles driven!")
    miles_driven = input("Please enter the amount of miles driven: ")

gallons_used = input("Please enter the amount of gallons used: ")
while not gallons_used.isdigit():
    print("You did not enter a valid number for the amount of gallons used!")
    gallons_used = input("Please enter the amount of gallons used: ")


print("Miles per gallon:", round(float(miles_driven) / float(gallons_used), 2))
