import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Regression Dataset Assignments\Students_Performance_Dataset.csv"
)

print("Head Records")
print(df.head())

print("Data shape")
print(df.shape)

print("Data information")
print(df.info())

print("Stat summary")
print(df.describe())

print("Missing Values")
print(df.isnull().sum())

# Convert Text into Numbers
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df["gender"] = encoder.fit_transform(df["gender"])
df["race/ethnicity"] = encoder.fit_transform(df["race/ethnicity"])
df["parental level of education"] = encoder.fit_transform(df["parental level of education"])
df["lunch"] = encoder.fit_transform(df["lunch"])
df["test preparation course"] = encoder.fit_transform(df["test preparation course"])

# Scatter Plot Graph
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x="reading score",
    y="math score"
)
plt.title("Reading Score vs Math Score")
plt.xlabel("Reading Score")
plt.ylabel("Math Score")
plt.show()

# Correlation Matrix
print("Correlation Matrix")
print(df.corr())

# Features and Target
X = df.drop("math score", axis=1)
y = df["math score"]

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
print("Model Train Start")


# Linear Regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
print("Model Train Complete")

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

print("Mean absolute error :", mae)
print("mean squared error :", mse)
print("Root Mean Squared Error :", rmse)
print("R2 score :", r2)
