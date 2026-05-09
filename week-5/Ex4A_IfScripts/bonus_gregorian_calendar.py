#create a script to determine whether a
#given year is a leap year in the Gregorian calendar. You will need to do a little research
#to determine exactly what makes a year a leap yea.
year = 2028

leap_year = year / 4

not_leap_year = year / 100
leap_year_2 = year / 400

# at frist i used the / to divide but i actually need to use % no remainder means leap year
if year % 4 == 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

#/ give the out put as is, % checks if something divides evenly 
# the == 0 means no remainder

