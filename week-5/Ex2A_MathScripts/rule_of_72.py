#5. How long will it take a savings account worth X to double in value based on an interest rate of IR? (Hint: Look up the “rule of 72”)
#savings x= 12000
#intrest rate  = 8%
#number of years t = 72/ intrest rate as %
#Your current savings is [number].
#At a [number]% interest rate, your savings account will be
#worth [number] in [number] years
savings = 12000
ir = 8 #percent
t = 72 / ir # t means years
worth = savings * 2
print('Your current savings is', (savings))
print(f'At a {ir}% interest rate, your savings account will be worth {worth: .2f} in {t: .1f} years.')

#lab 3
# using input() for savings 
savings = float(input('What is your current savings?'))
ir = float(input('What is the interest rate (only number)?')) #percent
t = 72 / ir # t means years
worth = savings * 2
print(f'Your current savings is {savings}')
print(f'At a {ir}% interest rate, your savings account will be worth {worth: .2f} in {t: .1f} years.')

# for this to work I had to add float first before i can add input(), input is a string and the float made it so i can calculate a number
