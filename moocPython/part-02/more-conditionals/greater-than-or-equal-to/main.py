first_number = int(input("Please type in the first number: "))
second_number = int(input("Please type in another number: "))

if first_number == second_number:
    print("The numbers are equal!")
elif first_number > second_number:
    print(f"The greater number was: {first_number}")
else:
    print(f"The greater number was: {second_number}")