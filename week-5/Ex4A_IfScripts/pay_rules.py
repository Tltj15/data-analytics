pay_rate = 17.30
hours_worked = 16
overtime = 1.5

#create a script to calculate gross pay given the variables
#pay_rate and hours_worked. If the person works more than 40 hours, pay the
#overtime hours at 1.5 times the rate of regular hours.
if hours_worked > 40:
    pay = pay_rate * 40
    over_hours = hours_worked - 40
    overtime_pay = over_hours * (pay_rate * overtime)
    gross_pay = pay + overtime_pay
    print('overtime pay is:', gross_pay, 'with', over_hours, 'hours overtime')    
else:
    gross_pay = pay_rate * hours_worked
    print('pay is:', gross_pay)


