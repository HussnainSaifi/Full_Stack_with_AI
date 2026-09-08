import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Regression Dataset Assignments\Salary_Dataset.csv"
)

print("First 5 records")
print(df.head())

print("Dataset Shape")
print(df.shape)

print("Dataset information")
print(df.info())

print("Stati summary")
print(df.describe())

print("Missing Values")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()

# Endocing
from sklearn.preprocessing import LabelEncoder

gender_encoder = LabelEncoder()
education_encoder = LabelEncoder()
job_encoder = LabelEncoder()

df["Gender"] = gender_encoder.fit_transform(df["Gender"])
df["Education Level"] = education_encoder.fit_transform(df["Education Level"])
df["Job Title"] = job_encoder.fit_transform(df["Job Title"])

# Graph

plt.figure(figsize=(7,5))

sns.scatterplot(
    data=df,
    x="Years of Experience",
    y="Salary"
)

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.show()

print("Correl matrix")
print(df.corr())

# Features and Target


X = df.drop("Salary", axis=1)
y = df["Salary"]

# Train Test Split

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Model Training Started...")

# Linear_regression_model

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

print("mean Absolute error :", mae)
print("mean Squared Error :", mse)
print("root mean squared error :", rmse)
print("R2 Score :", r2)
