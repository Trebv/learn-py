attempts = 0

while True:
    attempts += 1
    user_input = input("PIN: ")

    if user_input == "4321":
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")