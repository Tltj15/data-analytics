#calculate federal tax based on the values of annual gross income (a number) 
#and a filing status (‘single’ or ‘joint’)
pay_rate = 17.30
hours_worked = 50
overtime = 1.5
status = 'single'

# gross pay
if hours_worked > 40:
    pay = pay_rate * 40
    over_hours = hours_worked - 40
    overtime_pay = over_hours * (pay_rate * overtime)
    gross_pay = pay + overtime_pay   
else: 
    gross_pay = pay_rate * hours_worked

print ('You worked', hours_worked, 'this period')
print('Because you earn $', format(pay_rate, '.2f'), ',your gross weekly pay is $', format(gross_pay,'.2f'))

annuel = gross_pay * 52
#annual  52 weeks in a year
# use thsi to find t
if annuel < 12000:
    tax_rate = .05
elif annuel < 25000:
    tax_rate = .10
elif annuel < 75000:
    tax_rate = .15
else:
    tax_rate = .20

#finaly net pay
tax = gross_pay * tax_rate
net = gross_pay - tax
print('Your filling status is', status)
print('Your tax withholding for the week is $', format(tax,'.2f'))
print('Your net pay is $', format(net, '.2f'))