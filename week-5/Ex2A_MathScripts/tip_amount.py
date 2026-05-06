#3. How do you calculate the tip amount on a restaurant bill given the tip percentage?
#tip = total bill / tip percentage
#The tip on a $[number] restaurant bill is $[number]
total_bill = 97.50
tip_percent = .20
tip_dollar = total_bill * tip_percent
print(f'The tip on a $ {total_bill}  restaurant bill is $ {tip_dollar}')
