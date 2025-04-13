def factorial (n):
    if n < 2 :
        return 1
    else :
        fact = n * factorial( n - 1 )
        return fact
num = int(input('Enter a number : '))
print( f'Factorial of {num} is {factorial(num)}')
