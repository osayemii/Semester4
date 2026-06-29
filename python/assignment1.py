# Number 1
print('Number 1')

list1 = ['car', 'cycle', 'bus', 'car', 'scooter']
list2 = []

for item in list1:
    if item not in list2:
        list2.append(item)

print(', '.join(list2), '\n')


# Number 2
print('Number 2')

T1 = (2, 4, 6)
L1 = [1, 3, 5]

T1 = (2, 4, 6, L1)
for t1 in T1:
    if t1 == T1[-1]:
        print(t1, end='')
    else:
        print(t1, end=', ')

print('\n')


# Number 3
print('Number 3')

emp_dict = {
    'Name': 'Robert',
    'Age': 45,
    'Designation': 'Software Engineer',
    'Skills': ['C', 'Java', 'Ruby']
    }

emp_dict['Designation'] = 'Project Lead'
emp_dict['Skills'].append('Python')

for key, value in emp_dict.items():
    if key == 'Skills':
        print('Skills: ', end='')
        for skill in value:
            print(skill, end=', ')
    else:
        print(f'{key}: {value}')
print('\n')

# Number 4
print('Number 4')

mark_list = [35, 75, 86, 98]

for marks in mark_list:
    if marks > 90:
        print(f'{marks}: A')
    elif marks > 80:
        print(f'{marks}: B')
    elif marks > 70 :
        print(f'{marks}: C')
    elif marks > 0:
        print(f'{marks}: D')
    else:
        print('Invalid Mark')
print()


# Number 5
print('Number 5')

def func(product_result):
    if product_result > 300:
        pass
    else:
        print(product_result/10)

func(250)
func(480)
print()


# Number 6
print('Number 6')

var_num = 1
while var_num < 5:
    var_num = var_num+1
    if var_num == 2:
        continue
    print(var_num)

var_num = 0
while var_num < 5:
    var_num = var_num+1
    if var_num == 2:
        break
    print(var_num)