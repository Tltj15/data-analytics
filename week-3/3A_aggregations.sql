/* Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.*/
select ProductName, min(UnitPrice) as cheap_iteam
from products
group by ProductName
order by cheap_iteam;
-- geitost 2.5--

/* Write a query to find the average price of all items that Northwind sells.
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
using the ROUND function to round the average price to the nearest cent.)*/
select ProductName, round(avg(UnitPrice)) as avg_price 
from products
group by ProductName
order by avg_price ;

/* Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.*/
select ProductName, CompanyName, UnitPrice
from products
join suppliers on products.SupplierID = suppliers.SupplierID
order by UnitPrice desc
-- 'Cte de Blaye', 'Aux joyeux ecclsiastiques', '263.5000'--

/* Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries).*/
select round(sum(Salary))as monthly_payroll
from employees
-- $20363--

/* Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!).*/
select max(Salary) as max_salary, min(Salary) as min_salary
from employees
-- max $3119.15, min $1744.21 --

/* Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here.*/
select suppliers.CompanyName, suppliers.SupplierID, count(products.ProductID) as item_number
from suppliers
join products on products.SupplierID = suppliers.SupplierID
group by SupplierID, CompanyName
order by item_number;
-- 29rows returned --

/* Write a query to find the list of all category names and the average price for items in
each category.*/
select CategoryName, avg(UnitPrice) as avg_price
from categories
join products on products.CategoryID = categories.CategoryID
group by CategoryName
order by avg_price
-- 8rows returned--

/* Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.*/
select CompanyName, count(ProductID) as item_number
from suppliers
join products on products.SupplierID = suppliers.SupplierID
group by suppliers.SupplierID, CompanyName 
having count(ProductID) >= 5
-- 2rows returned --

/* Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.*/
select ProductID, ProductName, (UnitPrice * UnitsInStock) as inventory_value
from products
where UnitsInStock > 0
order by ProductName asc, inventory_value desc
-- 72rows returned, 2 or more have same value-- 

