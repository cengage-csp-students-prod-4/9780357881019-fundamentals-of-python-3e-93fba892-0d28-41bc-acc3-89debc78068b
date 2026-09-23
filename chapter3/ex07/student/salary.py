x= int(input("Enter the starting salary: "))
y= int(input("Enter the annual percent increase: "))
z= int(input("Enter the number of years: "))
print("\nYear   Salary\n----------------")
for i in range(1,z+1):
    print(format(i, "<7d") + format(x, "6.2f"))
    x = x * (1+y/100)
    