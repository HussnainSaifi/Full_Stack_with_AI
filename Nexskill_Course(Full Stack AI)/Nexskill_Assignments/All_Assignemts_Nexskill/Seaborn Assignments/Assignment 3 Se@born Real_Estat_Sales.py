import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Seaborn Assignments\Real_Estate_Sales_2001-2022_GL-Short.csv")

sns.set_style("whitegrid")

plt.figure()
sns.histplot(df["Sale Amount"])
plt.title("Sale Amount Distribution")
plt.show()

plt.figure()
sns.scatterplot(data=df, x="Assessed Value", y="Sale Amount")
plt.title("Assessed Value vs Sale Amount")
plt.show()

plt.figure()
sns.boxplot(data=df, x="Property Type", y="Sale Amount")
plt.title("Property Type vs Sale Amount")
plt.xticks(rotation=45)
plt.show()

plt.figure()
sns.boxplot(data=df, x="Residential Type", y="Sale Amount")
plt.title("Residential Type vs Sale Amount")
plt.xticks(rotation=45)
plt.show()

plt.figure()
sns.barplot(data=df, x="List Year", y="Sale Amount")
plt.title("List Year vs Sale Amount")
plt.show()

plt.figure()
sns.histplot(df["Sales Ratio"])
plt.title("Sales Ratio Distribution")
plt.show()