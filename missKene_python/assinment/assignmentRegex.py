import re


# Number 1
print("\nNumber 1")

emails = [
    'osayemi123@gmail.com',
    'lekan@mail.co',
    'daniel.com',
    'osadan11@mail.co'
]

for email in emails:
    result = re.search(r"\w+\d*@\w+.\w+", email)
    
    if result:
        print(email, ": Valid")
    else:
        print(email, ": Invalid")
        

# Number 2
print("\nNumber 2")

date = '31-12-2025'
result = re.split(r"-", date)
print(f"Date: {result[0]}, Month: {result[1]}, Year: {result[2]}")


# Number 3
print("\nNumber 3")

reg_rec = {
    'Name': 'John Paul',
    'Registration Number': 'CSC20250018',
    'Email': 'johnpaul@gmail.com',
    'Phone': '08034567891'
}

for value in reg_rec.values():
    reg_num = re.search(r'^[A-Za-z]+\d+$', value)
    phone = re.search(r'^\d{11}$', value)
    email = re.search(r'^\w+@\w+.\w+$', value)
    old_phone = re.search(r'\d{11}', value)
    new_phone = re.sub(r'\d{11}', '+2348034452595', value)
    
    if reg_num:
        print('Registration Number:', reg_num.group())
    if phone:
        print('Phone Number:', phone.group())
    if email:
        print('Email:', email.group())
    if old_phone:
        print(f'Replaced {old_phone.group()} with {new_phone}')
        
    