
# calculate the wages and how many hours work with overtime 

hours = input("enter hours:").split()

wage = int(input("Enter the wage:"))

week_hours = [int(x) for x in hours]

total_hours = sum(week_hours)

if total_hours <= 40:
    total_wage = total_hrs * wage 

else:
    overtime = total_hours - 40
    total_wage = 40 * wage + overtime * wage * 1.5
print("total wages:", total_wage)

