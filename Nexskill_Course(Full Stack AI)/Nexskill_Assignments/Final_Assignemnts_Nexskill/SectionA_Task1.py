# Section A - Task 1
# SpaceX Analytics (2010-2024)
# Full Stack AI Final Assessment

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Loading Dataset---

df = pd.read_csv(r"datasets/SpaceX_Analytics_2010_2024.csv")

print("\nDataset Loaded Successfully")

# ---------------------------------------------
# Display Dataset

print("\nFirst 5 Rows\n")
print(df.head())

print("\nLast 5 Rows\n")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

# --------------------------------------------
# Dataset Information

print("\nDataset Info\n")
print(df.info())

print("\nData Types\n")
print(df.dtypes)


# ------------------------------------------------

# Missing Values

print("\nMissing Values\n")

print(df.isnull().sum())

plt.figure(figsize=(10,5))
sns.heatmap(df.isnull(),cbar=False,cmap="viridis")
plt.title("Missing Values")
plt.show()

# ------------------------------------------------
# Duplicate Records

duplicates = df.duplicated().sum()

print("\nDuplicate Rows :",duplicates)

df = df.drop_duplicates()

print("\nShape After Removing Duplicate Rows")
print(df.shape)

# --------------------------------------------

# Descriptive Statistics

print("\nNumerical Statistics\n")

print(df.describe())

print("\nCategorical Statistics\n")

print(df.describe(include="object"))

# --------------------------------------------
# Encode Categorical Columns

encoder = LabelEncoder()

df["Company"] = encoder.fit_transform(df["Company"])

# ---------------------------------------------------
# Correlation Matrix

plt.figure(figsize=(10,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.show()

# ------------------------------------

# Distribution

df.hist(figsize=(15,10), bins=15)

plt.tight_layout()

plt.show()

# ---------------------------------------

# Boxplots

for column in df.select_dtypes(include="number").columns:

    plt.figure(figsize=(6,3))

    sns.boxplot(x=df[column])

    plt.title(column)

    plt.show()

    
# --------------------------------------------
 
# Pair Plot


sns.pairplot(df)

plt.show()

# --------------------------------------------

# Outlier Detection


numeric_df = df.select_dtypes(include="number")

Q1 = numeric_df.quantile(0.25)

Q3 = numeric_df.quantile(0.75)

IQR = Q3 - Q1

outliers = (
    (numeric_df < (Q1 - 1.5 * IQR))
    |
    (numeric_df > (Q3 + 1.5 * IQR))
).sum()

print(outliers)

# ---------------------------------------------
# Feature Selection

from sklearn.model_selection import train_test_split

# Input Features
X = df.drop("Success_Rate_%", axis=1)

# Target Variable
y = df["Success_Rate_%"]

print("\nFeatures Shape :", X.shape)
print("Target Shape :", y.shape)

# --------------------------------------------
# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data :", X_train.shape)
print("Testing Data :", X_test.shape)

# ------------------------------------------------------
# Feature Scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

print("\nFeature Scaling Completed")

# -----------------------------------------------
# Linear Regression

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()

linear_model.fit(X_train_scaled, y_train)

linear_predictions = linear_model.predict(X_test_scaled)

print("\nLinear Regression Model Trained")

# --------------------------------------------------
# Linear Regression Metrics

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, linear_predictions)

mse = mean_squared_error(y_test, linear_predictions)

rmse = mse ** 0.5

r2 = r2_score(y_test, linear_predictions)

print("\n---------------- Linear Regression -------------------")

print("MAE :", round(mae,2))
print("MSE :", round(mse,2))
print("RMSE :", round(rmse,2))
print("R2 Score :", round(r2,2))

# --------------------------------------------
# Prediction Comparison

comparison = pd.DataFrame({

    "Actual": y_test.values,

    "Predicted": linear_predictions

})

print(comparison.head(10))

# --------------------------------------------
# Actual vs Predicted Graph

plt.figure(figsize=(8,5))

plt.scatter(y_test, linear_predictions)

plt.xlabel("Actual Values")

plt.ylabel("Predicted Values")

plt.title("Linear Regression Prediction")

plt.grid(True)

plt.show()

# --------------------------------------------------
# Decision Tree Regressor

from sklearn.tree import DecisionTreeRegressor

tree_model = DecisionTreeRegressor(random_state=42)

tree_model.fit(X_train, y_train)

tree_predictions = tree_model.predict(X_test)

print("\nDecision Tree Model Trained")

# ------------------------------------------------
# Decision Tree Evaluation

tree_mae = mean_absolute_error(y_test, tree_predictions)

tree_rmse = mean_squared_error(y_test, tree_predictions) ** 0.5

tree_r2 = r2_score(y_test, tree_predictions)

print("\n---------------Decision Tree------------")

print("MAE :", round(tree_mae,2))

print("RMSE :", round(tree_rmse,2))

print("R2 Score :", round(tree_r2,2))

# -----------------------------------
# Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor

forest_model = RandomForestRegressor(

    n_estimators=100,

    random_state=42

)

forest_model.fit(X_train, y_train)

forest_predictions = forest_model.predict(X_test)

print("\nRandom Forest Model Trained")

# ---------------------------------------------
# Random Forest Metrics

forest_mae = mean_absolute_error(

    y_test,

    forest_predictions

)

forest_rmse = mean_squared_error(

    y_test,

    forest_predictions

) ** 0.5

forest_r2 = r2_score(

    y_test,

    forest_predictions

)

print("\n---------- Random Forest ---------------")

print("MAE :", round(forest_mae,2))

print("RMSE :", round(forest_rmse,2))

print("R2 Score :", round(forest_r2,2))

# ------------------------------------------------------------
# Model Comparison

results = pd.DataFrame({

    "Model":[

        "Linear Regression",

        "Decision Tree",

        "Random Forest"

    ],

    "R2 Score":[

        r2,

        tree_r2,

        forest_r2

    ]

})

print(results)

plt.figure(figsize=(7,4))

sns.barplot(

    data=results,

    x="Model",

    y="R2 Score"

)

plt.title("Regression Model Comparison")

plt.xticks(rotation=15)

plt.show()

# -------------------------------------------------------
# Create Target for Classification


df["Mission_Status"] = np.where(
    df["Success_Rate_%"] >= 90,
    "Successful",
    "Unsuccessful"
)

print(df["Mission_Status"].value_counts())

# -------------------------------------
# Encode Target Variable


label = LabelEncoder()

df["Mission_Status"] = label.fit_transform(df["Mission_Status"])

# Classification Dataset


X = df.drop(
    ["Success_Rate_%", "Mission_Status"],
    axis=1
)

y = df["Mission_Status"]

# ------------------------------------------------------------
# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

# ---------------------------------------------------

# Feature Scaling

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# ----------------------------------------------------------
# Logistic Regression

from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression()

log_model.fit(X_train_scaled, y_train)

log_prediction = log_model.predict(X_test_scaled)

print("Logistic Regression Completed")


# --------------------------------------------------------------------
# Accuracy Score

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(

    y_test,

    log_prediction

)

print("Accuracy :", accuracy)

# -----------------------------------------------------------
# Classification Report

from sklearn.metrics import classification_report

print(

    classification_report(

        y_test,

        log_prediction

    )

)


# ----------------------------------------------
# Confusion Matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(

    y_test,

    log_prediction

)

plt.figure(figsize=(5,4))

sns.heatmap(

    cm,

    annot=True,

    cmap="Blues",

    fmt="d"

)

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.title("Logistic Regression")

plt.show()


# -------------------------------------------------------------
# Decision Tree Classifier

from sklearn.tree import DecisionTreeClassifier

tree_classifier = DecisionTreeClassifier(

    random_state=42

)

tree_classifier.fit(

    X_train,

    y_train

)

tree_prediction = tree_classifier.predict(

    X_test

)

tree_accuracy = accuracy_score(

    y_test,

    tree_prediction

)

print("Decision Tree Accuracy :", tree_accuracy)


# -------------------------------------------------
# Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier

forest_classifier = RandomForestClassifier(

    n_estimators=100,

    random_state=42

)

forest_classifier.fit(

    X_train,

    y_train

)

forest_prediction = forest_classifier.predict(

    X_test

)

forest_accuracy = accuracy_score(

    y_test,

    forest_prediction

)

print("Random Forest Accuracy :", forest_accuracy)

# -----------------------------------------------------------
# Gradient Boosting

from sklearn.ensemble import GradientBoostingClassifier

gb_model = GradientBoostingClassifier()

gb_model.fit(

    X_train,

    y_train

)

gb_prediction = gb_model.predict(

    X_test

)

gb_accuracy = accuracy_score(

    y_test,

    gb_prediction

)

print("Gradient Boosting Accuracy :", gb_accuracy)


# ---------------------------------------------------
# Model Comparison

comparison = pd.DataFrame({

    "Model":[

        "Logistic Regression",

        "Decision Tree",

        "Random Forest",

        "Gradient Boosting"

    ],

    "Accuracy":[

        accuracy,

        tree_accuracy,

        forest_accuracy,

        gb_accuracy

    ]

})

print(comparison)

plt.figure(figsize=(8,4))

sns.barplot(

    data=comparison,

    x="Model",

    y="Accuracy"

)

plt.xticks(rotation=20)

plt.title("Classification Models")

plt.show()

# --------------------------------------------
# Feature Importance

importance = pd.DataFrame({

    "Feature":X.columns,

    "Importance":forest_classifier.feature_importances_

})

importance = importance.sort_values(

    by="Importance",

    ascending=False

)

print(importance)

plt.figure(figsize=(8,5))

sns.barplot(

    data=importance,

    x="Importance",

    y="Feature"

)

plt.title("Feature Importance")

plt.show()

# -----------------------------------------------------
# KMeans Clustering

from sklearn.cluster import KMeans

cluster_data = df.drop(["Mission_Status"], axis=1)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(cluster_data)

print("\nCluster Labels Added Successfully")
print(df["Cluster"].value_counts())

# -----------------------------------------------
# Elbow Method

wcss = []

for i in range(1, 11):

    model = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    model.fit(cluster_data)

    wcss.append(model.inertia_)

plt.figure(figsize=(8,5))

plt.plot(range(1,11), wcss, marker="o")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.title("Elbow Method")

plt.grid(True)

plt.show()

# ----------------------------------------------
# Cluster Visualization

plt.figure(figsize=(8,6))

sns.scatterplot(

    data=df,

    x="Launches",

    y="Revenue_USD_M",

    hue="Cluster",

    palette="Set1",

    s=120

)

plt.title("KMeans Clustering")

plt.show()

# ---------------------------------------------------------
# Cluster Summary

cluster_summary = df.groupby("Cluster").mean(numeric_only=True)

print(cluster_summary)

# -----------------------------------------------------
# Top Companies

top_company = df.sort_values(

    by="Revenue_USD_M",

    ascending=False

)

print(top_company.head(10))

# -------------------------------------------
# Revenue Distribution
# 

plt.figure(figsize=(8,5))

sns.histplot(

    df["Revenue_USD_M"],

    bins=10,

    kde=True

)

plt.title("Revenue Distribution")

plt.show()

# --------------------------------------
# Launches vs Success Rate

plt.figure(figsize=(8,5))

sns.scatterplot(

    data=df,

    x="Launches",

    y="Success_Rate_%",

    s=120

)

plt.title("Launches vs Success Rate")

plt.show()

# ---------------------------------------
# Revenue by Company

plt.figure(figsize=(10,5))

sns.barplot(

    data=df,

    x="Company",

    y="Revenue_USD_M"

)

plt.xticks(rotation=45)

plt.title("Revenue by Company")

plt.show()

# Final Dataset

print(df.head())

print(df.tail())

print(df.shape)


# Save Dataset


df.to_csv(

    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\Processed_SpaceX_Analytics_2010_2024.csv",

    index=False

)

print("\nProcessed dataset saved successfully.")