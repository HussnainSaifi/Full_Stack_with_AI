import pandas as pd
df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Pandas Assignments\FastFoodRestaurants.csv")

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

#  Head , Tail 
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

# Column pick
print("Access single column (name):")
print(df['name'])
print()

print("Access multiple columns:")
print(df[['name', 'city', 'province']])
print()

# Loc
print("LOC single row:")
print(df.loc[1])
print()

print("LOC multiple rows:")
print(df.loc[[1, 3]])
print()

print("LOC slice:")
print(df.loc[1:5])
print()

# Illoc
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

# Add new row
df.loc[len(df.index)] = df.iloc[0]  

print("New row added")
print(df.tail(2))
print()

# Dfop rows
df_clean = df.dropna()

print("After dropna:")
print(df_clean.head())
print()

# drop column
if 'country' in df.columns:
    df.drop('country', axis=1, inplace=True)
    print("Country column removed")

print()

# re name column
df.rename(columns={'name': 'restaurant_name'}, inplace=True)

print("Renamed columns:")
print(df.head())
print()

# query
result = df.query("city == city")  

print("Query result sample:")
print(result.head())
print()

# sort
if 'city' in df.columns:
    print("Sorted by city:")
    print(df.sort_values(by='city').head())

print()

# Group by
if 'city' in df.columns:
    grouped = df.groupby('city').size()
    print("Groupby city count:")
    print(grouped.head())