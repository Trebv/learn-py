gift = int(input("Value of git: "))

if gift >= 1000000:
    tax = (gift - 1000000)*0.17 + 142100
elif gift >= 200000:
    tax = (gift - 200000)*0.15 + 22100
elif gift >= 55000:
    tax = (gift - 55000)*0.12 + 4700
elif gift >= 25000:
    tax = (gift - 25000)*0.10 + 1700
elif gift >= 5000:
    tax = (gift - 5000)*0.08 + 100
else:
    tax = 0

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")