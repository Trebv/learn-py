user_pwd = input("Password: ")

while True:
    repeat_pwd = input("Repeat password: ")
    if repeat_pwd != user_pwd:
        print("They do not match!")
    else:
        print("User account created!")
        break