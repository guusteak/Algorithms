def factorial(number):
    #base case
    if number == 1:
        return 1
    else: 
        #recursion case
        return factorial(number-1) * number

print(factorial(5))
print(factorial(3))
print(factorial(10))