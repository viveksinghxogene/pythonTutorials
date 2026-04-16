import pandas as pd

data = {
    'Name': ['Aman', 'Riya', 'John', 'Sara', 'Kiran'],
    'Age': [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print(df)

print(df['Name'])
print(df[['Name', 'Marks']])

print(df.loc[0])
print(df.loc[1:3])

print(df.iloc[0:3])
print(df.iloc[:, 1:3])