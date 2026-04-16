import pandas as pd

df = pd.DataFrame({
    'Name': ['Aman', 'Riya', 'John', 'Sara', 'Kiran'],
    'Age': [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 88, 92]
})

print(df[['Name', 'Marks']])