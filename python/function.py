# User defined
def adam():
    print('Hello I am Prince')

adam()

# //Parametarised function
def name(name):
    print(f'Hello {name}')

def addition(num1, num2):
    sum = num1 + num2
    print(f'The sum of {num1} and {num2} is {sum}')

def course_func(name, course_name):
    print(f'Hi {name}! Welcome to the programming lab.')
    print(f'The name of your course is {course_name}')

input2 = 10 # global variable
def func_add1(input1):
    sum = input1 + input2
    print(f'Sum: {sum}')
inp1 = 5
func_add1(inp1)
print(f'Difference: {input2 - inp1}')

# Calling functions
name('Daniel')
name('Osayemi')

addition(10, 20)
addition(11, 30.5)

course_func('Olamilekan', 'Building Application with Flutter and Dart')