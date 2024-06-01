SELECT E1.name as Employee
FROM Employee E1
LEFT JOIN Employee E2
    ON E2.id = E1.managerId
WHERE E2.salary < E1.salary