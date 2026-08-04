import pandas as pd

# Dataframe from 2d array
data = [['Richard','M'],['Emy','F'],['Adam','M']]

df = pd.DataFrame(data, columns=['Name','Gender'])
print (df)


# Dataframe from object
data = {
    'Name': ['Richard', 'Emy', 'Adam'],
    'Gender': ['M', 'F', 'M']
}

df = pd.DataFrame(data)
print(df)