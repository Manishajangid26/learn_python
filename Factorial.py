# Write a function factorial() that calculates the factorial of a given non-negative integer.


def Factorial(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)
Factorial(5)    