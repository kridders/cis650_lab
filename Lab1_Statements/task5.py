first_number = input("Please enter the first number: ")
while not first_number.isdigit():
    print("You did not enter a valid number for the first number")
    first_number = input("Please enter the first number: ")

first_number = int(first_number)

second_number = input("Please enter the second number: ")
while not second_number.isdigit():
    print("You did not enter a valid number for the second number")
    second_number = input("Please enter the second number: ")

second_number = int(second_number)

if first_number > second_number:
    print (f"{first_number} is bigger than {second_number}.")
elif first_number == second_number:
    print(f"{first_number} is equal to {second_number}")
elif first_number < second_number:
    print (f"{first_number} is smaller than {second_number}")

