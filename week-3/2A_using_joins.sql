/* Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name.*/
select ProductID, ProductName, UnitPrice, CategoryName
from products 
join categories on products.CategoryID = categories.CategoryID
order by CategoryName, ProductName;
-- 77rows returned--

/* Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name.*/
select ProductID, ProductName, UnitPrice, CompanyName
from products
join suppliers on products.SupplierID = suppliers.SupplierID
where UnitPrice > 75
order by ProductName;
-- 4rows returned --

/* Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name.*/
select ProductID, ProductName, UnitPrice, CategoryName, CompanyName
from products
join suppliers on suppliers.SupplierID = products.SupplierID
join categories on categories.CategoryID = products.CategoryID
order by ProductName;

/* Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to.*/
select OrderID, ShipName, ShipAddress, ShipCountry, (CompanyName) as Shipper
from orders
join shippers on shippers.ShipperID = orders.ShipVia
where ShipCountry = 'Germany'
order by Shipper, ShipName;

/* Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name.*/
select ShipName, ShipAddress, ShipCountry, (CompanyName) as Shipper, count(OrderID) as TotalOrders
from orders
join shippers on shippers.ShipperID = orders.ShipVia
where ShipCountry = 'Germany'
group by ShipName , ShipAddress, ShipCountry, shipper
order by Shipper, ShipName
-- 32 rows returned --

/* Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale.
∗ Hint: You will need to join on three tables to accomplish this. (One of these tables
has a sneaky space in the name, so you will need to surround it with backticks, like
this: `table name`).*/
Select orders.OrderID, orders.OrderDate, orders.ShipName, orders.ShipAddress
from orders 
join `order details` on `order details`.OrderID = orders.OrderID
join products on products.ProductID = `order details`.ProductID
where ProductName = 'Sasquatch Ale'
-- 19rows returned--

-- select *
-- from `order details`
-- select *
--from products-- (productname= sasquatch)--



