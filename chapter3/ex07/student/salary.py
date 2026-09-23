# Salary growth table
# Shows how a starting salary grows each year with a fixed percent raise.

# Get the inputs from the user
x = int(input("Enter the starting salary: "))          # starting salary
y = int(input("Enter the annual percent increase: "))  # raise per year, as a percent (5 = 5%)
z = int(input("Enter the number of years: "))          # how many years to show

# Print the table header
print("\nYear   Salary\n----------------")

# Loop once for each year, from year 1 through year z
for i in range(1, z + 1):
    # Print the year (left-aligned, 7 characters wide) followed by
    # the salary (2 decimal places, 6 characters wide)
    print(format(i, "<7d") + format(x, "6.2f"))

    # Apply the raise so the next year starts from the new salary
    # (compounds: each raise is based on the previous year's salary)
    x = x * (1 + y / 100)