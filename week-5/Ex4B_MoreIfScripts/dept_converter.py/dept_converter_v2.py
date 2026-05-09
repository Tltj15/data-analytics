#using a match/case statement
#1 = Marketing
#5 = Human Resources
#10 = Accounting
#12 = Legal
#18 = IT
#20 = Customer Relations

def store_code(code):
    match code:
        case 5:
            print('Huamn Resources')
        case 10:
         print('Accounting')
        case 12:
            print('Legal')
        case 18:
            print('IT')
        case 20:
            print('Customer Relations')
        case 1:
            print('Marketing')
        case _:
            print('No department found')
store_code(20)

# with this one, it was a bit more confusing for me.
# im use to assigning value before the code and with one i had to assign at the end of the code for it to work.
# also i had to assign a variable before i could assign a value
#instead of def store_code(5) match 5, i had to assing the variable code then call on the value of the code store_code(5)