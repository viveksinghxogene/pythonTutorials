import pandas as pd

df = pd.read_csv('data.csv')
print(df)

df = pd.DataFrame({
    'Name': ['John', 'Sara'],
    'Marks': [78, 88]
})

df.to_csv('output.csv', index=False)