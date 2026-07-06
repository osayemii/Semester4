# DEFAULT ARGUMENT
def MyFuncDefault(empid, empname, department='Research'):
    print(f'The employee details are {empid}, {empname}, {department}')

MyFuncDefault(1, 'George Samuel')
MyFuncDefault(2, 'David Thomas', 'Tools')


def Student(fName):
    print(f'{fName} Dave')

Student('Emil')
Student('Mary')
Student('Jackson')
Student('Linus')


def addition(a=7, b=8):
    sum = a+b
    print(f'Sum: {a+b}')

addition(2, 3)
addition(a=4)
addition(b=2)
addition()


# POSITIONAL ARGUMENT
def add(a, b):
    return a+b
print(add(5, 10))

def minus(a, b):
    return a - b
a, b = 20, 10
answer = minus(a, b)
print(f"Correct order: {answer}")

answer = minus(b, a)
print(f'Incorrect order: {answer}')

# ----------------------------------
def minus(a, b):
    return a-b
a,b = 63,18
answer = minus(a,b)
print(f"Correct order: {answer}")

answer = minus(b, a)
print(f'Incorrect order: {answer}')

# ----------------------------------
def myFunction(name, age):
    print(f'My name is {name}, my age is {age}')

myFunction('Daniel', 10)
myFunction(10, 'Daniel')


# KEYWORD ARGUMENT
def Country(nation, food, color):
    print(f'My favourite country is {nation}')
    print(f'My favourite food is {food}')
    print(f'My favourite color is {color}')

Country(nation='Nambia', food='Rice', color='Blue')

# VARIABLE LENGTH ARGUMENT
# Arbitrary Positional Argument
def marks(name, *subject):
    total = 0
    for mark in subject:
        total += mark
    average = total / len(subject)
    print(f'Average mark of {name} is {average}')

marks('Dian', 20, 40, 19) # 'Dian' only belongs to 'name' while the rest belongs to 'subject'
marks('Joseph', 25, 45, 50, 11)

# Arbitrary Keyword Argument
def myMarks(name, **subject):
    total = 0
    for sub in subject:
        subject_name = sub
        subject_mark = subject[sub]
        total += subject_mark
        print(f'{subject_name}: {subject_mark}')
    print(f'Total marks for {name} is = {total}')

myMarks('Catherine', English = 10, Math = 16, Biology = 13)
myMarks('Meliodas', Chemistry = 15, Physics = 19,)