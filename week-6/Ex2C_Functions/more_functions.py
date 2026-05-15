#In the function output, format and display
#the data as you would on an address label.
def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f'{city}, {state}, {zip_code}')
    
display_mailing_label(name = 'Mary Jane', address = '123 St.', city = 'Detroit', state= 'Michigan', zip_code= 30025)
display_mailing_label(name= 'John Doe', address= '2456 N. Perry Ln', city= 'Kenosha', state= 'Wisconsin', zip_code= 96321)

#In the function,
#add given arguments together and display the result using the following format:
#number [+ number2 + number3 ...] = result
def add_numbers(*args):
    #use the *agrs functions to accept any number of agruments
    #type(args) is a tuple
    total = sum(args) #add the numbers
    numbers_str = ' ' #string of numbers
    for i, num in enumerate(args): #for loop
        numbers_str = numbers_str + str(num)
        if i < len(args) - 1:
            numbers_str = numbers_str + ' + ' #this is the format output
    print(f'{numbers_str} = {total}')

add_numbers(2, 4, 6)
add_numbers(5)
add_numbers(6, 8)

#Compute and display the change due in the following format:
#Total Due: $_____
#Amount Paid: $_____
#Change Due: $____
#If the amount paid is less than the total due, display a message indicating the
#remaining balance to be paid.
def display_receipt(total_due, amount_paid):
    print(f'Total due:$ {total_due:.2f}')
    print(f'Amount paid:$ {amount_paid:.2f}')
    if amount_paid < total_due:
        remaining = total_due - amount_paid
        print(f'You have a remaining balance:$ {remaining:.2f}')
    elif amount_paid > total_due:
        change = amount_paid - total_due
        print(f'Change due:$ {change:.2f}')
    else: 
        print('No change due')

display_receipt(total_due= 68.09, amount_paid= 80)
display_receipt(total_due= 75.25, amount_paid= 75.25)
display_receipt(total_due= 36, amount_paid= 30)
    

    















