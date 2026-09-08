import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Seaborn Assignments\FastFoodRestaurants.csv")

sns.set_style("whitegrid")

# City count
sns.countplot(data=df, y="city")
plt.title("City Count")
plt.show()

# Province count
sns.countplot(data=df, y="province")
plt.title("Province Count")
plt.show()

# Latitude
sns.histplot(df["latitude"])
plt.title("Latitude")
plt.show()

# Longitude
sns.histplot(df["longitude"])
plt.title("Longitude")
plt.show()

# Top names
top = df["name"].value_counts().head(5)
sns.barplot(x=top.values, y=top.index)
plt.title("Top Names")
plt.show()