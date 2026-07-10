def oddOrEven(n):
    if n <= 0:
        return
    elif n%2 != 0:
        print(f"{n} : Odd")
        oddOrEven(n-1)
    else:
        print(f"{n} : Even")
        oddOrEven(n-1)
        
number = int(input("Enter a range: "))
oddOrEven(number)