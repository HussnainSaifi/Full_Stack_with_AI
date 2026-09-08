import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
data = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Classification Dataset Assignments\Multivariate Gait Data.csv"
)

print(data.head())

# Display total records for each condition
plt.figure(figsize=(7, 5))
sns.countplot(data=data, x="condition", hue="condition", palette="Set2", legend=False)
plt.title("Condition Distribution")
plt.xlabel("Condition")
plt.ylabel("Frequency")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Input and output columns
features = data[["subject", "replication", "leg", "joint", "time", "angle"]]
target = data["condition"]

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.20,
    random_state=42
)

print("Training the model")

# Create classifier
rf = RandomForestClassifier(random_state=42)

# Train
rf.fit(x_train, y_train)

# Predict
predictions = rf.predict(x_test)

# Accuracy
acc = accuracy_score(y_test, predictions)

print("Accuracy :", round(acc * 100, 2), "%")

print("Confusion Matrix")
print(confusion_matrix(y_test, predictions))

print("Classification Report")
print(classification_report(y_test, predictions))
