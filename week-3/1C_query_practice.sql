/* Write a query to list the product id, product name, and unit price of every product. This
time, display them in ascending order by price.*/
select ProductID, ProductName, UnitPrice
from products
order by UnitPrice asc;

/* What are the products that we carry where we have at least 100 units on hand? Order
them in descending order by price.*/
select ProductID, ProductName, UnitPrice, UnitsInStock
from products
where UnitsInStock >= 100
order by UnitPrice desc;
-- 10rows returned--

/* What are the products that we carry where we have at least 100 units on hand? Order
them in descending order by price. If two or more have the same price, list those in
ascending order by product name.*/
select ProductID, ProductName, UnitPrice, UnitsInStock
from products
where UnitsInStock >= 100
and UnitsInStock 
order by UnitPrice desc, ProductName asc;

/* Write a query against the orders table that displays the total number of distinct
customers who have placed orders, based on customer ID. Use an alias to label the
count calculation as CustomerCount.*/
select ShipCountry, count(distinct CustomerID) as CustomerCount
from orders
group by ShipCountry
order by CustomerCount desc;
-- 21rows returned--

/* What are the products that we carry where we have less than 25 units on hand, but 1
or more units of them are on order? Write a query that orders them by quantity on
order (high to low), then by product name.*/
select ProductName, UnitsInStock, UnitsOnOrder
from products
where UnitsInStock < 25
and UnitsOnOrder > 0
order by ProductName, UnitsOnOrder desc;
-- 17rows returned--

/*Write a query to list each of the job titles in employees, along with a count of how
many employees hold each job title.*/
select Title, count(*) as EmployeeCount
from employees
group by Title
order by EmployeeCount desc
-- 4rows returned--

/* What employees have a monthly salary that is between $2000 and $2500? Write a
query that orders them by job title.*/
select EmployeeID, Title, Salary
from employees
where Salary between 2000 and 2500
order by Title desc;
-- 4rows returned--














