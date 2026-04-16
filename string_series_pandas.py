import pandas as pd

courses = pd.Series(['Java', 'Python', 'AWS'])

print(courses)
print(courses.str.upper())
print(courses.str.contains('y'))