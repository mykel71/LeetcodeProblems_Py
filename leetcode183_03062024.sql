SELECT c.name as Customers
FROM Customer c
WHERE c.id NOT IN (SELECT
                        o.customerId
                    FROM Orders o)