import pandas as pd

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Pandas Assignments\RealEstate-USA (1).csv")
print(df)
print()

print("Head")
print(df.head())
print()

print("Tail")
print(df.tail())
print()

print("Shape")
print(df.shape)
print()

print("Columns")
print(df.columns)
print()

print("Data types")
print(df.dtypes)
print()

print("Info")
print(df.info())
print()

print("Describe")
print(df.describe())
print()

# Selecting column
if 'City' in df.columns:
    print(df['City'])
    print()

# Multiple columns
if 'City' in df.columns and 'Address' in df.columns:
    print(df[['City', 'Address']])
    print()

# loc
print("Loc single row")
print(df.loc[1])
print()

print("Loc multiple rows")
print(df.loc[[1, 5]])
print()

print("Loc slicing")
print(df.loc[0:5])
print()

# iloc
print("Iloc single row")
print(df.iloc[1])
print()

print("Iloc multiple rows")
print(df.iloc[[0, 2, 4]])
print()

print("Iloc slicing")
print(df.iloc[0:5])
print()

# drop null values
print("Dropping null values")
df_clean = df.dropna()
print(df_clean.head())
print()

# rename column (if exists)
if 'Price' in df.columns:
    df.rename(columns={'Price': 'Property_Price'}, inplace=True)
print()

# query example
if 'Property_Price' in df.columns:
    result = df.query("Property_Price > 500000")
    print(result.head())
print()

# sort values
if 'City' in df.columns:
    print(df.sort_values(by='City').head())
print()

# groupby
if 'City' in df.columns:
    grouped = df.groupby('City').size()
    print(grouped.head())