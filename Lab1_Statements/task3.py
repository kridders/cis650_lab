first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

#First name check
while len(first_name) == 0:
    print("Your first name is empty. Please enter a valid name!")
    first_name = input("Please enter your first name: ")


#Last name check
while len(last_name) == 0:
    print("Your last name is empty. Please enter a valid name!")
    last_name = input("Please enter your last name: ")


#Output
print("Hello,", first_name, last_name)
