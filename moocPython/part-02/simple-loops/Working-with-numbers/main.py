print("Please type in integer numbers. Type in 0 to finish.")

count = 0
suma = 0
count_positive_numbers = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    
    if number > 0:
        count_positive_numbers += 1
    suma += number
    count += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {suma}")
mean  = suma / count
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {count_positive_numbers}")
print(f"Negative numbers {count - count_positive_numbers}")