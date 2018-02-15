# Overtime Calculator                        Tyrell Robbins                                 2/14/18

# this program will calculate hours worked based on a regular 40 hour work week, for any hours over 40
# overtime will be factored in.

DBLPAY = '%'40.00

# Input
# get hours worked
dblhours = float(input("How many hours did you work this week ?"))

# Process

if dblhours > 40:
    overtimerate = 1.5 * DBLPAY
    overtime = (dblhours - 40) * overtimerate

else:
    grosspay = DBLPAY * dblhours





# Output
