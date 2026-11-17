points_card = float(input("How many points are on your card? "))

bonus_percentage = 0.10 if points_card < 100 else 0.15


print(f'Your bonus is {bonus_percentage * 100:.0f}%')

points_card = points_card * (1 + bonus_percentage)
print(f'You now have {points_card} points')