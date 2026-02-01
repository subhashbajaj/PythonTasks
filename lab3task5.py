import pandas as pd

dict = {
    "country": ["Brazil", "Russia", "India"],
    "capital": ["Brasilia", "Moscow", "New Delhi"],
    "area": [8.516, 17.10, 3.286],
    "population": [200.4, 143.5, 1252]
}

df = pd.DataFrame(dict)
print(df)
df = pd.DataFrame({
    'Date': ['11/05/19', '12/05/19', '19/05/19'],
    'Time Worked': [3, 3, 4],
    'Money Earned': [33.94, 33.94, 46.0]
})

print(df.head())