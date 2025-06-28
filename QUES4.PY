import pandas as pd


df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Eve'],
    'Salary': [50000, 75000,67500,60000,82000],
    'City':     ['New York','London',' ','Paris','Tokyo'],
    'Experience':[3,7,15,7.5,5]
})

median_salary = df['Salary'].median()
df['Salary'].fillna(median_salary, inplace=True)
df['City'] = df['City'].str.strip().replace('', 'Unknown')
print(df)
