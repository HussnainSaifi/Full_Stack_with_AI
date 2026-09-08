import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Regression Dataset Assignments\Advertising_Dataset.csv"
)

print("1-5 Records")
print(df.head())

print("Dataset_Shape")
print(df.shape)

print("Dataset_Information")
print(df.info())

print("Stat-Summary")
print(df.describe())

print("Missing-Values")
print(df.isnull().sum())

# Graphs

plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="TV", y="Sales")
plt.title("TV vs Sales")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Radio", y="Sales")
plt.title("Radio vs Sales")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Newspaper", y="Sales")
plt.title("Newspaper vs Sales")
plt.show()

print("Correlation")

print(df.corr())

# Feature & Target

X = df[["TV","Radio","Newspaper"]]

y = df["Sales"]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Model Training!")

# Linear-Regression

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

print(result.head(10))

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE :", rmse)
print("R2 Score :", r2)
