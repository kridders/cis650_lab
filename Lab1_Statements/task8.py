alphabets = 'abcdefghijklmnopqrstuvwxyz'
while True:
    user_entry = input("Enter a letter (or blank to exit): ")
    if user_entry == " ":
        break
    else:
        position = alphabets.find(user_entry)
        if position < 0:
            print("Character not found!")
        else:
            print(f'{user_entry} is at position {position}')


