import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\Seaborn Assignments\startup_growth_investment_data.csv")

print(df.head())
print()

sns.set_style("whitegrid")

#Growth-rate distribution
plt.figure()
sns.histplot(df["Growth Rate (%)"], kde=True)
plt.title("Growth Rate Distribution")
plt.show()

# Investment-amount vs valuation
plt.figure()
sns.scatterplot(data=df, x="Investment Amount (USD)", y="Valuation (USD)")
plt.title("Investment vs Valuation")
plt.show()

#funding rounds and growth rate
plt.figure()
sns.boxplot(data=df, x="Funding Rounds", y="Growth Rate (%)")
plt.title("Funding Rounds vs Growth Rate")
plt.show()

#Investors count distribution
plt.figure()
sns.histplot(df["Number of Investors"], bins=10)
plt.title("Number of Investors Distribution")
plt.show()

# Country wise average growth
plt.figure()
sns.barplot(data=df, x="Country", y="Growth Rate (%)")
plt.title("Country vs Growth Rate")
plt.xticks(rotation=45)
plt.show()

#Industry vs Investment
plt.figure()
sns.barplot(data=df, x="Industry", y="Investment Amount (USD)")
plt.title("Industry vs Investment")
plt.xticks(rotation=45)
plt.show()