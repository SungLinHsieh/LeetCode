# Write your MySQL query statement below
SELECT Name AS 'Customers'
FROM Customers
LEFT OUTER JOIN Orders
ON Customers.Id=Orders.CustomerId
WHERE CustomerId IS NULL
