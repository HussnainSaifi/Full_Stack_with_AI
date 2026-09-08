import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load Dataset

products = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Classification Dataset Assignments\pricerunner_aggregate.csv"
)

# Remove spaces from column names
products.columns = products.columns.str.strip()

print("First 5 Records")
print(products.head())

print("\nDataset Shape")
print(products.shape)

print("\nColumn Names")
print(products.columns)

print("\nMissing Values")
print(products.isnull().sum())
# Graph

plt.figure(figsize=(10,5))

sns.countplot(
    data=products,
    x="Category Label",
    order=products["Category Label"].value_counts().index,
    hue="Category Label",
    palette="Set3",
    legend=False
)

plt.xticks(rotation=90)
plt.title("Products Category")
plt.xlabel("Category")
plt.ylabel("Total Products")
plt.tight_layout()
plt.show()

# Encoding

from sklearn.preprocessing import LabelEncoder

title_encoder = LabelEncoder()
cluster_encoder = LabelEncoder()
target_encoder = LabelEncoder()

products["Product Title"] = title_encoder.fit_transform(products["Product Title"])

products["Cluster Label"] = cluster_encoder.fit_transform(products["Cluster Label"])

products["Category Label"] = target_encoder.fit_transform(products["Category Label"])

# Features and Target
X = products[
    [
        "Product ID",
        "Product Title",
        "Merchant ID",
        "Cluster ID",
        "Cluster Label"
    ]
]

y = products["Category Label"]

# Train Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Model...")
# Random Forest

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Completed")
# Prediction

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy")
print(round(accuracy * 100, 2), "%")

print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("Classification Report")
print(classification_report(y_test, y_pred))
