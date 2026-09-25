salary = int(input("Enter the starting salary: $"))
percent = int(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

print("\nYear   Salary")
print("-------------")

for year in range(1, years + 1):
    print(f"{year:>2}    {salary:.2f}")
    salary = salary * (1 + percent / 100)