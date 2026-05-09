#use if/elif/else logic to determine
#and print department name based on a department code. Make sure to test your
#script with multiple codes.
#1 = Marketing
#5 = Human Resources
#10 = Accounting
#12 = Legal
#18 = IT
#20 = Customer Relations
store_code = 18

if store_code == 5:
    print('Human Resorces')
elif store_code == 10:
    print('Accounting')
elif store_code == 12:
    print('Legal')
elif store_code == 18:
    print('IT')
elif store_code == 20:
    print('Customer Relations')
elif store_code == 1:
    print('Marketing')
else:
    print('No department found?')    





