import pandas as pd

df = pd.DataFrame({
    'Name': ['Vivek', 'Manasvi', 'Harsh'],
    'Marks': [85, 90, 78]
})

print(df.loc[1, 'Name'])