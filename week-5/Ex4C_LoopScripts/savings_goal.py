#Create a variable for your starting bank balance, another that sets your savings goal,
#and a third with your weekly savings amount.
#Use a while loop to compare your bank balance to your savings goal, if you haven’t
#met your goal yet, add the weekly savings amount to your bank balance. For each loop,
#print the statement, “This week my balance increased to ___.” Once your savings goal
#is met, print the statement, “Goal met! My current balance is ___.”
starting_bal = 750
savings_goal = 2000
weekly_savings = 78
half_way = False

while starting_bal <= savings_goal:
    starting_bal = starting_bal + weekly_savings
    print('This is week my balance increased to', starting_bal)

#print('Goal met! My current balance is', starting_bal)

# had to fix the script initinally i had, print('This is week my balance increased to', starting_bal + weeklysavings)
#which was causing my loop to go on past the saving goal


#added 50% of goal reached
    if starting_bal >= savings_goal * .50 and not half_way:
        print('Almost there! This week my balance is up to', starting_bal)
        half_way = True

print('Goal met! My current balance is', starting_bal)

# had issues had to use 'and' with a true or false.
#everything had to be inside the while loop to function
