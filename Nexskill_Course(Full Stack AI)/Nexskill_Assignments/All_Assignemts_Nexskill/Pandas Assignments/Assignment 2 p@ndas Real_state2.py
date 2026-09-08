import pandas as pd
df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Pandas Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv")
print(df)
print()

# Head and Tail

print("Head ",df.head())
print()
print("Tail ", df.tail())
print()

print("Type, info, describe, shape")
print(df.dtypes)
print()

print(df.info)
print()

print(df.describe)
print()

print(df.shape)
print()

# Selecting column
print("Picking single column from df")
print(df["Location"])
print()

print("Multiple column at same time")
print(df[['Town','Address']])
print()

# Loc
print("Loc single row")
print(df.loc[1])
print()

print("loc on multiple rows")
print(df.loc[[1, 8]])
print()

print("Loc slicing")
print(df.loc[0:10])
print()

# Iloc

print("Iloc single row")
print(df.iloc[0])
print()

print("Iloc on multiple rows")
print(df.iloc[[1, 4, 5, 7, 9]])
print()

print("Iloc slicing")
print(df.iloc[1:5])

# Adding new row
df.loc[len(df.index)] = df.iloc[1]
print(df.tail(3))
print()

# drop rows wit nan values
print("drows rows of nan")
dro = df.dropna()
print(dro)
print()

# drop column
if 'List Year' in df.columns:
    df.drop('List Year', axis=1, inplace=True)
    print("List Year removed")
print()

# re-name column
df.rename(columns={'Serial Number': 'Sr_No'}, inplace=True)
print(df.head())
print()

# query
rt = df.query("Sr_No == 20058")  
print(rt.head())
print()

# Sort
if 'Town' in df.columns:
    print(df.sort_values(by='Town').head())
print()

# Group-by
if 'Address' in df.columns:
    grouped = df.groupby('Address').size()
    print(grouped.head())