import pandas as pd

# Series
color = pd.Series(['red', 'blue', 'green', 'yellow', 'white'])
print(color)

# Dictionary--------------------------------------------

dict = {
    'name': 'Daniel',
    'age': 12,
    'city': 'Kubwa'
}

ser = pd.Series(dict)
print(ser)


# Series with Index----------------------------------------

num_ser = pd.Series(50, index=[1, 2, 3, 4, 5])
print(num_ser)