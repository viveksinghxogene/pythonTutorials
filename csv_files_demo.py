import pandas as pd

df = pd.DataFrame({
    'Name': ['Aman', 'Riya'],
    'Marks': [85, 90]
})

df.to_csv('data.csv', index=False)