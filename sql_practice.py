### Nth highest

# Highest
'''
SELECT Max(Salary)
FROM Employees
'''

# Second highest from sub query
'''
SELECT Max(Salary)
FROM Employees
WHERE Salary <
    (SELECT Max(Salary) FROM Employees)
'''

'''
SELECT DISTINCT TOP 2 Salary
FROM Employees
ORDER BY Salary DESC
'''
 # Top nth - change '2' to be nth
'''
SELECT TOP 1 Salary
FROM
    (SELECT DISTINCT TOP 2 Salary  
    FROM Employees
    ORDER BY Salary DESC) Result
ORDER BY Salary
'''
 # applying rank
'''
Select Salary, DENSE_RANK () over (ORDER BY Salary DESC) as DENSERANK
FROM Employees