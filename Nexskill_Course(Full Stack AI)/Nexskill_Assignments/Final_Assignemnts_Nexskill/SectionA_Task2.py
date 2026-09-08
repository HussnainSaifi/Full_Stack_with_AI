# Section A - Task 2
# SpaceX Missions Dataset

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# --------------------------------------------------
# Load Dataset

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\datasets\Space x Missions.csv")

print(df.head())

print(df.shape)

print(df.info())

print("\nMissing Values")

print(df.isnull().sum())

plt.figure(figsize=(10,5))

sns.heatmap(df.isnull(), cmap="viridis", cbar=False)

plt.title("Missing Values")

plt.show()

print("\nDuplicate Rows :", df.duplicated().sum())

df = df.drop_duplicates()

print(df.shape)




# Payload Mass
df["Payload Mass (kg)"] = df["Payload Mass (kg)"].fillna(
    df["Payload Mass (kg)"].median()
)

# Payload Type
df["Payload Type"] = df["Payload Type"].fillna("Unknown")

# Payload Orbit
df["Payload Orbit"] = df["Payload Orbit"].fillna("Unknown")

# Customer Name
df["Customer Name"] = df["Customer Name"].fillna("Unknown")

# Customer Type
df["Customer Type"] = df["Customer Type"].fillna("Unknown")

# Customer Country
df["Customer Country"] = df["Customer Country"].fillna("Unknown")

# Failure Reason
df["Failure Reason"] = df["Failure Reason"].fillna("No Failure")

# Landing Type
df["Landing Type"] = df["Landing Type"].fillna("Not Attempted")

# Landing Outcome
df["Landing Outcome"] = df["Landing Outcome"].fillna("Unknown")

df["Launch Date"] = pd.to_datetime(df["Launch Date"])

df["Launch Year"] = df["Launch Date"].dt.year

df["Launch Month"] = df["Launch Date"].dt.month

print(df.head())

print(df.describe(include="all"))



# Graphs---------------

plt.figure(figsize=(10,5))

sns.countplot(

    data=df,

    x="Launch Year"

)

plt.xticks(rotation=45)

plt.title("Launches Per Year")

plt.show()

plt.figure(figsize=(7,5))

sns.countplot(

    data=df,

    x="Mission Outcome"

)

plt.title("Mission Outcome")

plt.show()

plt.figure(figsize=(10,5))

sns.countplot(

    data=df,

    y="Launch Site"

)

plt.title("Launch Site")

plt.show()


plt.figure(figsize=(10,5))

sns.countplot(

    data=df,

    x="Vehicle Type"

)

plt.xticks(rotation=20)

plt.show()


plt.figure(figsize=(8,5))

sns.histplot(

    df["Payload Mass (kg)"],

    kde=True

)

plt.title("Payload Mass Distribution")

plt.show()



# Encoding---------------------------
encoder = LabelEncoder()

categorical_columns = df.select_dtypes(include="object").columns

for col in categorical_columns:

    df[col] = encoder.fit_transform(df[col])

print(df.head())

plt.figure(figsize=(14,8))

sns.heatmap(

    df.corr(numeric_only=True),

    annot=True,

    cmap="coolwarm"

)

plt.title("Correlation Matrix")

plt.show()

# ==========================================
# Regression
# Target = Payload Mass (kg)
# ==========================================

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X = df.drop(
    ["Payload Mass (kg)", "Launch Date"],
    axis=1
)
y = df["Payload Mass (kg)"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

tree_reg = DecisionTreeRegressor(random_state=42)

tree_reg.fit(X_train, y_train)

tree_pred = tree_reg.predict(X_test)

print("\nDecision Tree Regression")

print("MAE :", round(mean_absolute_error(y_test, tree_pred),2))

print("RMSE :", round(mean_squared_error(y_test, tree_pred)**0.5,2))

print("R2 :", round(r2_score(y_test, tree_pred),2))

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

tree_reg = DecisionTreeRegressor(random_state=42)

tree_reg.fit(X_train, y_train)

tree_pred = tree_reg.predict(X_test)

print("\nDecision Tree Regression")

print("MAE :", round(mean_absolute_error(y_test, tree_pred),2))

print("RMSE :", round(mean_squared_error(y_test, tree_pred)**0.5,2))

print("R2 :", round(r2_score(y_test, tree_pred),2))

from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_reg.fit(X_train, y_train)

rf_pred = rf_reg.predict(X_test)

print("\nRandom Forest Regression")

print("MAE :", round(mean_absolute_error(y_test, rf_pred),2))

print("RMSE :", round(mean_squared_error(y_test, rf_pred)**0.5,2))

print("R2 :", round(r2_score(y_test, rf_pred),2))


regression_results = pd.DataFrame({

    "Model":[

        "Decision Tree",

        "Random Forest"

    ],

    "R2 Score":[

        r2_score(y_test, tree_pred),

        r2_score(y_test, rf_pred)

    ]

})

print(regression_results)

plt.figure(figsize=(7,4))

sns.barplot(

    data=regression_results,

    x="Model",

    y="R2 Score"

)

plt.title("Regression Comparison")

plt.show()


# Classification
# Target = Mission Outcome


X = df.drop(
    ["Mission Outcome", "Launch Date"],
    axis=1
)

y = df["Mission Outcome"]

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)



# knn calisifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train_scaled, y_train)

knn_pred = knn.predict(X_test_scaled)

knn_accuracy = accuracy_score(

    y_test,

    knn_pred

)

print("\nKNN Accuracy :", knn_accuracy)



#SVM
from sklearn.svm import SVC

svm = SVC()

svm.fit(

    X_train_scaled,

    y_train

)

svm_pred = svm.predict(

    X_test_scaled

)

svm_accuracy = accuracy_score(

    y_test,

    svm_pred

)

print("SVM Accuracy :", svm_accuracy)


# report
from sklearn.metrics import classification_report

print(

    classification_report(

        y_test,

        svm_pred

    )

)


#Confusion Martix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(

    y_test,

    svm_pred

)

plt.figure(figsize=(5,4))

sns.heatmap(

    cm,

    annot=True,

    cmap="Blues",

    fmt="d"

)

plt.title("SVM Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()


# Compare
classification_results = pd.DataFrame({

    "Model":[

        "KNN",

        "SVM"

    ],

    "Accuracy":[

        knn_accuracy,

        svm_accuracy

    ]

})

print(classification_results)

plt.figure(figsize=(6,4))

sns.barplot(

    data=classification_results,

    x="Model",

    y="Accuracy"

)

plt.title("Classification Comparison")

plt.show()


# -----------------------------------------
# KMeans Clustering

from sklearn.cluster import KMeans

cluster_data = df.drop(
    ["Launch Date"],
    axis=1
)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(cluster_data)

print("\nCluster Distribution")
print(df["Cluster"].value_counts())

# ---------------------------------------------------
# Elbow Method

wcss = []

for i in range(1,11):

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

# ---------------------------------------------------
# Cluster Visualization

plt.figure(figsize=(8,6))

sns.scatterplot(

    data=df,

    x="Launch Year",

    y="Payload Mass (kg)",

    hue="Cluster",

    palette="Set2",

    s=120

)

plt.title("Mission Clusters")

plt.show()

# ---------------------------------------------------------
# AdaBoost Classifier

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

base_model = DecisionTreeClassifier(max_depth=1)

ada = AdaBoostClassifier(

    estimator=base_model,

    n_estimators=50,

    random_state=42

)

ada.fit(X_train, y_train)

ada_prediction = ada.predict(X_test)





from sklearn.metrics import accuracy_score

ada_accuracy = accuracy_score(

    y_test,

    ada_prediction

)

print("\nAdaBoost Accuracy :", ada_accuracy)

comparison = pd.DataFrame({

    "Model":[

        "KNN",

        "SVM",

        "AdaBoost"

    ],

    "Accuracy":[

        knn_accuracy,

        svm_accuracy,

        ada_accuracy

    ]

})

print(comparison)

plt.figure(figsize=(7,4))

sns.barplot(

    data=comparison,

    x="Model",

    y="Accuracy"

)

plt.title("Classification Models Comparison")

plt.show()

# Cluster Summery
cluster_summary = df.groupby("Cluster").mean(numeric_only=True)

print(cluster_summary)


# Save
df.to_csv(

    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\Processed_Space x Missions.csv",

    index=False

)

print("\nProcessed dataset saved successfully.")