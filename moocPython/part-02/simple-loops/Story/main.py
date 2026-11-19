text_user = ""
while True:
    user_input = input("Please type in a word: ")
    
    if user_input == "end":
        break
    
    if len(text_user) > 0:
        if user_input == text_user.split()[-1]:
            break
    text_user += user_input + " "

print(text_user)