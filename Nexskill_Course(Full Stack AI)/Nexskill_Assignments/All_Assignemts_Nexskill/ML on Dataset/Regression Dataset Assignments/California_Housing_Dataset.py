import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Regression Dataset Assignments\California_Housing_Dataset.csv"
)

print("5 head record")
print(df.head())

print("Dataset shape")
print(df.shape)

print("Dataset information")
print(df.info())

print("Stats summary")
print(df.describe())

print("Missing values")
print(df.isnull().sum())

# Handling missing value

df["total_bedrooms"] = df["total_bedrooms"].fillna(
    df["total_bedrooms"].mean()
)

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

df["ocean_proximity"] = encoder.fit_transform(df["ocean_proximity"])

# Scatter plot graph

plt.figure(figsize=(7,5))

sns.scatterplot(
    data=df,
    x="median_income",
    y="median_house_value"
)

plt.title("Median Income vs House Value")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")

plt.show()

# Correl matrix

print("Corre Matrix")

print(df.corr())

# Featuring and Targeting

X = df.drop("median_house_value", axis=1)

y = df["median_house_value"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Linear regression model

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Training Complete")

# Prediction

y_pred = model.predict(X_test)

result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print("Prediction Result")
print(result.head(10))

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
