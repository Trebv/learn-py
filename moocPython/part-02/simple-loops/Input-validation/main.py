from math import sqrt

while True:
    number_user = int(input("Please type in a number: "))

    if number_user == 0:
        print("Exiting...")
        break
    elif number_user > 0:
        print(f"{sqrt(number_user)}")
    else:
        print("Invalid number")