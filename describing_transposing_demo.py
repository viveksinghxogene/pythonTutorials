import pandas as pd

df = pd.DataFrame({
    'Marks': [85, 90, 78, 88],
    'Age': [21, 22, 20, 23]
})

print(df.describe())
print(df.T)