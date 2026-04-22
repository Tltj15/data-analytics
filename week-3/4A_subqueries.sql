/* What is the product name(s) of the most expensive products?
∗ HINT: Find the max price in a subquery and then use that value to find products
whose price equals that value. (Some of your answers from Exercise 3.A may offer a
useful starting point.)*/
select ProductName, max(UnitPrice) as max_item
from products
group by ProductName
order by max_item desc;
-- Cte de Blaye $263.500, Thringer Rostbratwurst $123.79, Mishi Kobe Niku $97.00 --

/* What is the product name(s) and categories of the least expensive products?
∗ HINT: Find the min price in a subquery and then use that in your more complex
query that joins products with categories.*/
select ProductName, CategoryName, min(UnitPrice) as lowest
from products
join categories on categories.CategoryID = products.CategoryID
group by ProductName, CategoryName
order by lowest;
-- Geitost- Dairy Products $2.50, Guaran Fantstica-Beverages $4.50, Konbu- Seafood $6.00 --

/* What is the order id, shipping name and shipping address of all orders shipped via
"Federal Shipping"?
∗ HINT: Find the shipper id of "Federal Shipping" in a subquery and then use that
value to find the orders that used that shipper.
∗ You do not need "Federal Shipping" to display in the results.*/
select OrderID, ShipName, ShipAddress
from orders
join shippers on shippers.ShipperID = orders.ShipVia
where CompanyName = 'Federal Shipping'

/* What are the order ids of the orders that included "Sasquatch Ale"?
∗ HINT: Find the product id of "Sasquatch Ale" in a subquery and then use that value
to find the matching orders from the `order details` table.
∗ Your final results only need to display OrderID, but you may find it helpful to include
additional columns as you work on creating the query to better understand how the
query is working.*/
select ProductID, ProductName
from products 
where ProductName like 'Sasq%';
-- product id 34 --

select OrderID
from `order details`
where ProductID = 34
-- 19rows returned --

-- What is the name of the employee that sold order 10266? --
select EmployeeID, LastName, FirstName
from employees
where EmployeeID = (
	select EmployeeID 
    from orders
    where OrderID = 10266
    );
-- 3. janet leverling --
    
-- What is the name of the customer that bought order 10266? --
select CustomerID, CompanyName, ContactName
from customers
where CustomerID = (
	select CustomerID
    from orders
    where OrderID = 10266
    );
    -- WARTH, Wartian Herkku, Pirkko Koskitalo --

