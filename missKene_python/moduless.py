import math
import random

print(f"The sqaure root of 25 is {math.sqrt(25)}")
print(f"The exponential of 25 is {math.exp(25)}")

def func(x):
    print(f"Sqare root of {x} is {math.sqrt(value)}")
    print(f"Exponential of {x} is {math.exp(value)}")
    
value = int(input('Enter a number: '))
func(value)


# ---------------------------------------------------
number = 25
print("Square Root =", math.sqrt(number))
print("Factorial =", math.factorial(5))
print("Power =", math.pow(2,5))

# Excercise: Generate five random numbers
import random

for i in range(5):
    print(random.randint(1, 100))