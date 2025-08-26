numbers = []
while True:
    input_number = input("Please enter a number (use blank to exit): ")
    if input_number == " ":
        break
    else:
        while not input_number.isdigit():
            print("You did not enter a valid number. Please try again! ")
            input_number = input("Please enter a digit number (use blank to exit): ")
        numbers.append(int(input_number))


numbers.sort()
print(f"The lowest of all the input numbers was: {numbers[0]}")