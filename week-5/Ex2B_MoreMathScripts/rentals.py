#6. There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
#$250 per day to rent (including the driver’s pay). How many vans do you need? How
#much will it cost to rent vans? What is the cost if you split it per person?

tourists = 38
van_seat = 15
van_cost = 250
vans_needed = tourists / van_seat
print('We need', round(vans_needed), 'vans')
total_cost = round(vans_needed) * van_cost
print('$', total_cost, 'for the vans')
split_cost = total_cost / tourists
print('It will cost $', round(split_cost), 'per person')

#a) How much money did your script say you had to charge per person?
# $20 per person
#b) If you multiply that out, how much did you collect?
print('$',round(split_cost) * tourists, 'was collected for the vans')
#c) How much were the vans?
#$750 for the vans
#d) Why do you have leftover money?
# have $10 left over since we have to cover for the full van regardless if all 15 seats are being used or not by the number of tourists. 
