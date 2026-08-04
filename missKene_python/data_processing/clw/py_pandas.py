import pandas as pd

# Number 2
sales = {
    'year1': 200000,
    'year2': 310000,
    'year3': 670000,
    'year4': 1300000,
}

output = pd.Series(data=sales)
print(output)

# Number 3
sch_data = {
    'student_name': ['Daniel', 'OSayemi', 'Olamilekan'],
    'course': ['ADSE', "Cyber Security", 'Web Developer'],
    'Score': [32, 75, 98]
}

output = pd.DataFrame(data=sch_data)
print(output)

# Number 4
csv_file = pd.read_csv('data_processing\Product_Sales.csv')

# Number 5
print(csv_file.head(15))

# Number 6
print(csv_file.tail(12))

# Number 7
print(csv_file.describe())