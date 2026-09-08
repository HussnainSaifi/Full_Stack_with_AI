import pandas as pd

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Pandas Assignments\startup_growth_investment_data.csv")
print(df)
print()

print("Data type of df")
print(df.dtypes)
print()

print("Data info of df")
print(df.info())
print()

print("Describe (statistics)")
print(df.describe(include='all'))
print()

# Head and Tail
print("Head and Tail")

print("Tail:")
print(df.tail(5))
print()

print("Head:")
print(df.head(7))
print()

# Shape
print("Shape:", df.shape)
print()

# Column access
print("Single column:")
if 'Startup Name' in df.columns:
    print(df['Startup Name'])
print()

print("Multiple columns:")
cols = [col for col in ['Startup Name', 'Industry', 'City'] if col in df.columns]
print(df[cols])
print()

# LOC
print("LOC single row:")
print(df.loc[1])
print()

print("LOC multiple rows:")
print(df.loc[[1, 3]])
print()

print("LOC slice:")
print(df.loc[1:5])
print()

# ILOC
print("ILOC single row:")
print(df.iloc[0])
print()

print("ILOC multiple rows:")
print(df.iloc[[1, 3, 5]])
print()

print("ILOC slice:")
print(df.iloc[0:5])
print()

print("ILOC columns:")
print(df.iloc[:, 0:3])
print()

# Add row
df.loc[len(df.index)] = df.iloc[0]
print("New row added")
print(df.tail(2))
print()

# Drop NaN
df_clean = df.dropna()
print("After dropna:")
print(df_clean.head())
print()

# Drop column
if 'Country' in df.columns:
    df.drop('Country', axis=1, inplace=True)
    print("Country column removed")
print()

# Rename column
if 'Startup Name' in df.columns:
    df.rename(columns={'Startup Name': 'Startup'}, inplace=True)
    print("Column renamed")
print()

print(df.head())
print()

# Query
if 'Investment Amount' in df.columns:
    result = df.query("`Investment Amount` > 1000000")
    print("Query result sample:")
    print(result.head())
print()

# Sort
if 'City' in df.columns:
    print("Sorted by City:")
    print(df.sort_values(by='City').head())
print()

# Groupby
if 'City' in df.columns:
    grouped = df.groupby('City').size()
    print("Groupby City count:")
    print(grouped.head())