numbers = []

for i in range(1,6):
    new_number = input(f"Please enter the {i}. number:  ")
    while not new_number.isdigit():
        print("You did not enter a valid number. Please try again! ")
        new_number = input(f"Please enter the {i}. number:  ")
    numbers.append(int(new_number))

numbers.sort()

print(f"The lowest of all the input numbers was: {numbers[0]}")
