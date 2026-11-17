times = int(input("How many times a week do you eat at the student cafeteria? "))
price_lunch = float(input("The price of a typical student lunch? "))
money_groceries = float(input("How much money do you spend on groceries in a week? "))

print(f"Average food expenditure: ")
print(f"Daily: {(money_groceries + (times * price_lunch))/7} euros")
print(f"Weekly: {(price_lunch * times) + money_groceries} euros")