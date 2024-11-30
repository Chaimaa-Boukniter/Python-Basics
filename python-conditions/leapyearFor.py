first_year = int (input("Enter the first year : "))
last_year = int (input("Enter the last year : "))
for year in range (first_year,last_year+1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
else :
    print(f"{year} isn't a leap year")
