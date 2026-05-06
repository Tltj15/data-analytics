#1. How do you calculate your net worth given your assets and debts?
#your total assets are 
#your total debts are
#your net worth is 
assets = {'cash': 5000, 'savings': 7000, 'car': 8000, 'investments': 11000}
debts = {'credit_card': 2000, 'student_loan': 9000}

#networht=assets-debt
total_assets = sum(assets.values())
total_debts = sum(debts.values())
net_worth = total_assets - total_debts

print('Your total assets are', total_assets)
print('Your total debts are', total_debts)
print('Your total net worth is', net_worth)

