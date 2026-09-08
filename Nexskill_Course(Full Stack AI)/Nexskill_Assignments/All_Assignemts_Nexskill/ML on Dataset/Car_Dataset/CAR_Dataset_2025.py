import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Car_Dataset\Cars Datasets 2025.csv",encoding="latin1")
print(df)
# Head
print("Head ",df.head())
# Tail
print("Tail ",df.tail())
# Describe
print("Describe ",df.describe())
# Info
print("Info ",df.info())
# Mising Values
print(df.isnull().sum())
# Remove Duplicate
print(df.duplicated())
df = df.drop_duplicates()

# Cleaning cc/battery
df["CC"] = df["CC/Battery Capacity"].str.replace(',', '')
df["CC"] = df["CC"].str.extract(r"(\d+)")
df["CC"] = pd.to_numeric(df["CC"], errors="coerce")
df["CC"] = df["CC"].fillna(0)
print(df["CC"].astype(int))
 #------------------------------------------------CC/ Battery  Clean

# Horse Power cleaning
df["Horse_Power"] = df["HorsePower"].str.extract(r"(\d+)")
df["Horse_Power"] = pd.to_numeric(df["Horse_Power"])
print(df["Horse_Power"]) #------------------------------------------Horse_Power column is clean

# Total Speed
df["Total_speed"] = df["Total Speed"].str.extract(r"(\d+)")
df["Total_speed"] = pd.to_numeric(df["Total_speed"])
print(df["Total_speed"])  #----------------------------------------------Total_Speed is clean

# Performance(0 - 100 )KM/H
df["Performance"] = df["Performance(0 - 100 )KM/H"].str.extract(r"(\d+)")
df["Performance"] = pd.to_numeric(df["Performance"])
print(df["Performance"]) #---------------------------------------Performance column is clear

# Cars Prices
df["Car_Prices"] = df["Cars Prices"].replace('[\$,]', '', regex=True)
df["Car_Prices"] =pd.to_numeric(df["Car_Prices"], errors='coerce')
print(df["Car_Prices"]) #--------------------------------------------------Car_Prices clear

# Seats
df["All_Seats"] = pd.to_numeric(df["Seats"], errors="coerce")
df["All_Seats"] = df["All_Seats"].fillna(0)
print(df["All_Seats"].astype(int)) #---------------------------------------------------Seats clear column

# Torque
df["Torque_force"] = df["Torque"].str.extract(r"(\d+)")
df["Torque_force"] = pd.to_numeric(df["Torque_force"])
print(df["Torque_force"]) #----------------------------------------------------Torque cloumn is clear

# Value handle
df_clean = df[[
    "All_Seats",
    "Torque_force",
    "Car_Prices",
    "Performance",
    "Total_speed",
    "Horse_Power",
    "CC"
]].fillna(0)

# Csv
# df_clean.to_csv("All Assignments/ML on Dataset/Clean_Car_Dataset.csv")

plt.figure(figsize=(18,18))
sns.heatmap(df_clean.corr(), annot=True)
plt.show()

from sklearn.model_selection import train_test_split
X = df_clean[[
    "All_Seats",
    "Torque_force",
    "Performance",
    "Total_speed",
    "Horse_Power",
    "CC"
]]
Y = df_clean["Car_Prices"]
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train,Y_train)
Y_Predict = model.predict(X_test)

results = pd.DataFrame({
    "Actual": Y_test,
    "Predicted": Y_Predict
})
print(results)