# Overtime Calculator                        Tyrell Robbins                                 2/14/18

# this program will calculate hours worked based on a regular 40 hour work week, for any hours over 40
# overtime will be factored in.

DBLPAY = 40.00

# Input
# get hours worked
dblhours = float(input("How many hours did you work this week ?"))

# Process

if dblhours > 40:
    overtimerate = 1.5 * DBLPAY
    pay = 1600+(dblhours - 40) * overtimerate
    flag = 1
else:
    pay = DBLPAY * dblhours
    flag = 0

# Output

if(flag == 1):
    print("Gross pay with overtime",pay)
    print("Overtime Hours",dblhours - 40)
else:
    print("Gross pay without overtime",pay)

print("Hours worked",dblhours)
print("Pay",pay)
print("Hours Overtime", dblhours - 40)