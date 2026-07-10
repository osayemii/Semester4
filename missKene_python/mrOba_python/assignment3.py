# Number 1
print('Number 1')

def number1(num1, num2, num3, num4):
    return  num1 + num2 + num3 + num4

total = number1(num1=5, num2=3, num3=8, num4=4)
print(total)

# Number 2
print('\nNumber 2')
def number2(num1, num2, num3):
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    num3 = int(input('Enter number 3: '))

    print(f'Difference: {num1 - num2}')
    print(f'Product: {num3 * num2}')

number2(35, 11, 15)


# Number 3
print('\nNumber 3')

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return 'Try again'
    
print(max_num(4, 5, 6))


# Number 4
print('\nNumber 4')
def number4():
    words = ["Python", "Java", "Ruby", "Perl", "JavaScript"]
    for word in words:
        if len(word) == 4:
            print(word)

number4()


# Number 5
print('\nNumber 5')

x = 20
def outer_fun():
    x = 10

    def inner_fun():
        y = 20
        print(x + y)

    inner_fun()
print(x)
outer_fun()

def function1(var1, var2 = 5):
    var3 = var1 * var2
    return var3

var1 = 3
print(function1(var1=5,var2=6))
print(function1(var1,var2=6))
print(function1(var1,var2=3))