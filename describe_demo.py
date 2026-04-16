import pandas as pd

data = pd.Series([10, 20, 30, 40, 50, 60, 70])

print(data)
print(data.describe())

df = pd.DataFrame({
    'marks': [78, 85, 96, 88, 76],
    'age': [20, 21, 19, 22, 20]
})

print(df)
print(df.describe())