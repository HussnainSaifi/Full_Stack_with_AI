import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Classification Dataset Assignments\Predict Students' Dropout and Academic Success.csv",
    sep=";"
)

print("Dataset Loaded Successfully")
print(data.head())

print("Total Rows and Columns:")
print(data.shape)

print("Checking Missing Values")
print(data.isnull().sum())

print("Target Classes")
print(data["Target"].value_counts())


plt.figure(figsize=(8,5))

sns.countplot(
    x=data["Target"],
    palette="pastel"
)

plt.title("Students Category")
plt.xlabel("Category")
plt.ylabel("Number of Students")

plt.show()


from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

target = encoder.fit_transform(data["Target"])

features = data.drop(columns=["Target"])

# Split Dataset

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.20,
    random_state=10
)

print("Training Samples :", len(x_train))
print("Testing Samples :", len(x_test))


from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=150,
    random_state=10
)

print("Train Model on")

rf_model.fit(x_train, y_train)

print("Training Compl")


# Prediction


predicted = rf_model.predict(x_test)

# Performance


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

score = accuracy_score(y_test, predicted)

print("Accuracy :", round(score * 100,2), "%")

print("Confusion Matrix")

print(confusion_matrix(y_test, predicted))

print("Classification Report")

print(classification_report(y_test, predicted))


