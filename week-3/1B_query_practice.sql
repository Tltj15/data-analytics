/* Write a query to list the product id, product name, and unit price of every product that
Northwind sells. (Hint: To help set up your query, look at the schema preview to see
what column names belong to each table. Or use SELECT * to query all columns
first, then refine your query to just the columns you want.*/
use northwind
select ProductID, ProductName, UnitPrice
from products 

--Write a query to identify the products where the unit price is $7.50 or less.--
select ProductID, ProductName, UnitPrice
from products 
where UnitPrice <= 7.5

/* What are the products that we carry where we have no units on hand, but 1 or more
units are on backorder? Write a query that answers this question.*/
select ProductID, ProductName
from products
where UnitsInStock = 0
and UnitsOnOrder > 0

/* Examine the products table. How does it identify the type (category) of each item
sold? Where can you find a list of all categories? Write a set of queries to answer these
questions, ending with a query that creates a list of all the seafood items we carry.*/
-- The products table uese categoryID as a foreign key to join the categories tables.--
select *
from categories

select *
from products

select ProductName
from products
join categories on products.CategoryID = categories.CategoryID
where CategoryName = 'Seafood'
-- 12rows returned--

/* Examine the products table again. How do you know what supplier each product
comes from? Where can you find info on suppliers? Write a set of queries to find the
specific identifier for "Tokyo Traders" and then find all products from that supplier.*/
-- The prodcuts table has a supplier id and there is a suppliers table with a supplier id join.--
select *
from products

select *
from suppliers

select ProductName
from Products
join suppliers on suppliers.SupplierID = products.SupplierID
where CompanyName = 'Tokyo Traders'
-- 3rows returned--

/* How many employees work at northwind? What employees have "manager"
somewhere in their job title? Write queries to answer each question.*/
select *
from employees
-- 9rows returned--

select *
from employees
where Title like '%Manager%'
-- only one Steven employeeid 5--












