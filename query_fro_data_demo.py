import pandas as pd

df = pd.DataFrame({
    'Name': ['Aman', 'Riya', 'John', 'Sara', 'Kiran'],
    'Marks': [85, 90, 78, 88, 92]
})

print(df.query('Marks > 85'))