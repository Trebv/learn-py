year = int(input("Year: "))
next_leap_year = year + 1

while True:
    is_next_leap_year = False

    if next_leap_year % 4 == 0:
        is_next_leap_year = True
        if next_leap_year % 100 == 0:
            if next_leap_year % 400 != 0:
                is_next_leap_year = False

    if is_next_leap_year:
        print(f"The next leap year after {year} is {next_leap_year}")
        break
    else:
        next_leap_year += 1