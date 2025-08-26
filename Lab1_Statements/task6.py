numbers = []

for i in range(1,6):
    numbers.append(int(input(f"Please enter the {i}. number: ")))

numbers.sort()

print(f"The lowest of all the input numbers was: {numbers[0]}")
