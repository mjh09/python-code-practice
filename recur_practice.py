def factorial(n):
  if n == 0:
    return 1

  else:
    recurse = factorial(n-1)
    result = n * recurse
    return result

# factorial(3)
"""
since is not 0, calculate the factorial of n-1
  since 2 is not 0, calculate the factorial of n-1
    since 1 is not 0, calculate the factorial of n-1
      since 0 == 0, return 1
    the return value 1 is multiplied by n"1", return 1
  the return value 1 is multiplied by n"2", return 2
the reutnr value 2 is multiplied by n"3", return 6
"""
#https://en.wikipedia.org/wiki/Fibonacci_number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if not isinstance(n,int):
        print("factorial funct is only defined for integers")
        return None
    elif n < 0:
        print(" factorial funct is not defined for negative integers")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)