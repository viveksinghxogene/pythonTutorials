import pandas as pd

df = pd.DataFrame({
    'Name': ['Aman', 'Riya', 'John'],
    'Marks': [85, 90, 78]
})

print(df.sort_values(by='Marks'))