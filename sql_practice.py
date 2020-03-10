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