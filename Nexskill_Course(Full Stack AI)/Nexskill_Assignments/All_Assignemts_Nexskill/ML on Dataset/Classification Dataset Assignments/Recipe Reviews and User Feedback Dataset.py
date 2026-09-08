import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\All_Assignemts\ML on Dataset\Classification Dataset Assignments\Recipe Reviews and User Feedback Dataset.csv"
)

print("First Five Records")
print(data.head())

print("Shape")
print(data.shape)

print("Columns")
print(data.columns)

print("Missing Values")
print(data.isnull().sum())

# Graph
plt.figure(figsize=(7,5))

sns.countplot(
    data=data,
    x="stars",
    hue="stars",
    legend=False,
    palette="Set2"
)

plt.title("Rating Distribution")
plt.xlabel("Stars")
plt.ylabel("Number of Reviews")

plt.show()
# Encoding

from sklearn.preprocessing import LabelEncoder

recipe_encoder = LabelEncoder()
user_encoder = LabelEncoder()

data["recipe_name"] = recipe_encoder.fit_transform(data["recipe_name"])

data["user_name"] = user_encoder.fit_transform(data["user_name"])

# Features and Target

X = data[
    [
        "recipe_number",
        "recipe_code",
        "recipe_name",
        "user_reputation",
        "reply_count",
        "thumbs_up",
        "thumbs_down",
        "best_score"
    ]
]

y = data["stars"]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Train Model")

# Random Forest

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Complet")

# Prediction

prediction = model.predict(X_test)


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

accuracy = accuracy_score(y_test, prediction)

print("Accuracy")
print(round(accuracy*100,2),"%")

print("Confusion Matrix")
print(confusion_matrix(y_test,prediction))


print("Classification Report")
print(classification_report(y_test,prediction))
