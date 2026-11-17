hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day = input("Day of the weel: ")

daily_wages = hourly_wage * hours_worked if day != "Sunday" else (2 * hourly_wage * hours_worked)
print(f"Daily wages: {daily_wages} euros")