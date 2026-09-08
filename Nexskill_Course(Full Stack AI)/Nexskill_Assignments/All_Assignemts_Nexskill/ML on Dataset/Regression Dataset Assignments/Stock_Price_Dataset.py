import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_excel(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Regression Dataset Assignments\Stock_Price_Dataset.xlsx"
)

print("head records")
print(df.head())

print("Dataset-shape")
print(df.shape)

print("Dataset information")
print(df.info())

print("Statis Summary")
print(df.describe())

print("Missing Values")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()

# Scatter Plot Graph
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x="Open",
    y="Close*"
)

plt.title("Open Price vs Close Price")
plt.xlabel("Open Price")
plt.ylabel("Close Price")

plt.show()

# Correlation Matrix
print("Correlation Matrix")
numeric_df = df.select_dtypes(include=["number"])
print(numeric_df.corr())


# Features and Target
X = df[
    [
        "Open",
        "High",
        "Low",
        "Adj Close**",
        "Volume"
    ]
]
y = df["Close*"]

# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
print("Model Training Starts")

# Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
print("Model Training Completed")

# Prediction
y_pred = model.predict(X_test)
result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})
print("Prediction Result")
print(result.head(10))

# Sk-Learn Apply
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error :", mae)
print("Mean Squared Error :", mse)
print("Root Mean Squared Error :", rmse)
print("R2 Score :", r2)
