#You have been given the following list of sales records. Each record is a tuple
#containing a salesperson's name, their region, and their total sales for the month:
sales_data = [('Marcus Webb', 'East', 4250.00), ('Priya Sharma', 'West', 5875.50), 
              ('DeShawn Carter', 'East', 3100.75), ('LaTonya Rivers', 'South', 6420.00), 
              ('Bob Nguyen', 'West', 4980.25)]
for name, region, total in sales_data:
    print(f'{name}, ({region}): ${total}')

    if total > 5000:
        print('^Top performer!')



# had to use the fstring for print with () around {region} other wise it will just show region with no ()
