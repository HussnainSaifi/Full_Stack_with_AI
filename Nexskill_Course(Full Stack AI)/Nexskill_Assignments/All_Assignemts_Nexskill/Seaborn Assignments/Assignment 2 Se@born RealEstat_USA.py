import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Seaborn Assignments\RealEstate-USA (1).csv")

sns.set_style("whitegrid")

plt.figure()
sns.histplot(df["price"])
plt.title("Price Distribution")
plt.show()

plt.figure()
sns.scatterplot(data=df, x="house_size", y="price")
plt.title("House Size vs Price")
plt.show()

plt.figure()
sns.boxplot(data=df, x="bed", y="price")
plt.title("Bedrooms vs Price")
plt.show()

plt.figure()
sns.barplot(data=df, x="city", y="price")
plt.xticks(rotation=45)
plt.title("City vs Price")
plt.show()