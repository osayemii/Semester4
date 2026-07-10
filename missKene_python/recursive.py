print("Number 1")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number: "))
print("Factorial =",factorial(num))


print("\nNumber 2")
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
    
countdown(10)


print("\nNumber 3")
def even_sum(n):
    if n <= 0:
        return 0
    elif n%2 == 0:
        return n + even_sum(n - 2)
    else:
        return even_sum(n - 1)
    
num = int(input("Enter a number: "))
print("Sum of even numbers =", even_sum(num))