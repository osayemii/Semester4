a = 34
b = 200
if b > a:
    print('B is greate than A')

# ///////////////
age = 20
if age >= 18:
    print('You are an adult.\nYou can vote!\nYou have legal rights.')

# ///////////////
deborah = True
if deborah:
    print('Welcome back to tec-terminal')

# ///////////////
number = 16
if number > 0:
    print('The number is positive')

# ///////////////
age = 25
if age > 18:
    print('Eligible to vote!')
else:
    print('Too young to vote!!')

# ///////////////
_a = 48
_b = 48

if _b > _a:
    print('B is greater than A')
elif _b == _a:
    print('Both B and A are equal')
else:
    print('A is greater than B')

# ////////////////
day = 8

match day:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    
    case _:
        print('It is a lovely day')

# //////////////////
numbers = (3, 6, 7, 8, 10, 20, 15, 18, 19)
for number in numbers:
    a = number % 2
    if a == 0:
        print(number)
    else:
        print(f'{number} is not an even number')