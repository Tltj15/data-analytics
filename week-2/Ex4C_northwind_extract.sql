/*
4.a) products table has names of products they sell 
b) categories tables has what items fall under as well a description
*/

/*
5)Create a SELECT statement to retrieve all columns from the employees table.
a) Who is the Northwind employee whose name makes it look like she’s a bird?
Include the answer as a comment underneath the SELECT statement
*/
select * 
from northwind.employees; 
-- MRS.PEACOCK has a bird name--

/*
6)Create a SELECT statement to retrieve all columns from the products table.
a) How many records does your query return? Using the toolbar options at the top of
the query pane, how can you change your query to retrieve only 10 rows? Include
the answer as a comment underneath the SELECT statement.
b) BONUS: How could you write the query to limit the number of rows returned? This
isn’t covered in the Week 2 Student Guide, so if you tackle this bonus question,
you’ll need to do a little independent research. Add the answer as a comment in
your script with a note on what source you used to find the answer.
*/
select * 
from northwind.products;
-- 77 products--
-- by going to the limit tab and clicking on limit to 10 rows--
-- select * from northwind.prodcuts limit 10 --
/*
b) using the limit clause and number of amount of returns. I used the YUU SQL powerpoint as as source
*/

/*
7)Create another SELECT statement to retrieve all columns from the categories table.
c) What is the category id of seafood? Include a comment in your script to answer
this.
*/
select *
from northwind.categories
-- seafood categoryID is 8--

/*
8)Create a final SELECT statement to retrieve the top 50 records from orders, including
only the OrderID, OrderDate, ShipName, and ShipCountry columns.
a) Export the resulting record set to .csv format as Ex4C_order_sample.csv and save it
to week-02
*/
select OrderID, OrderDate, ShipName, ShipCountry
from orders
limit 50





