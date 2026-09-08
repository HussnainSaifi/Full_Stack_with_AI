# Section B - Task 4
# Deep Learning
# Dataset : spacex_launches.csv

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import GRU

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\datasets\spacex_launches.csv")

print(df.head())

print(df.info())

df["details"] = df["details"].fillna("No Details")

df["landing_type"] = df["landing_type"].fillna("Unknown")

print(df.isnull().sum())

#Date Formating

df["date_utc"] = pd.to_datetime(df["date_utc"])

df = df.sort_values("date_utc")

df.reset_index(drop=True, inplace=True)

df["Launch_Year"] = df["date_utc"].dt.year

df["Launch_Month"] = df["date_utc"].dt.month


plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="landing_success"
)

plt.title("Landing Success")

plt.show()

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="rocket_name"
)

plt.xticks(rotation=20)

plt.show()


plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    x="Launch_Year"
)

plt.xticks(rotation=45)

plt.show()

#Encoding

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

columns = [

    "name",

    "rocket_id",

    "rocket_name",

    "launchpad_id",

    "launchpad_name",

    "details",

    "landing_type"

]

for col in columns:

    df[col] = encoder.fit_transform(df[col])

#Featuring

features = [

    "flight_number",

    "rocket_name",

    "success",

    "failures",

    "crew_count",

    "payloads_count",

    "cores_reused",

    "Launch_Year",

    "Launch_Month"

]

X = df[features]

y = df["landing_success"]

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)


sequence = 5

X_data = []

y_data = []

for i in range(sequence, len(X_scaled)):

    X_data.append(X_scaled[i-sequence:i])

    y_data.append(y.iloc[i])

X_data = np.array(X_data)

y_data = np.array(y_data)

print(X_data.shape)

print(y_data.shape)


#Split

split = int(len(X_data)*0.80)

X_train = X_data[:split]

X_test = X_data[split:]

y_train = y_data[:split]

y_test = y_data[split:]

# ---------------------------------------------
# Simple RNN Model

rnn_model = Sequential()

rnn_model.add(
    SimpleRNN(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1], X_train.shape[2])
    )
)

rnn_model.add(Dense(1, activation="sigmoid"))

rnn_model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history_rnn = rnn_model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    validation_data=(X_test, y_test),
    verbose=1
)

loss, accuracy = rnn_model.evaluate(X_test, y_test, verbose=0)

print("\nRNN Accuracy :", round(accuracy * 100, 2), "%")


# ----------------------------------------------------
# LSTM Model

lstm_model = Sequential()

lstm_model.add(
    LSTM(
        32,
        input_shape=(X_train.shape[1], X_train.shape[2])
    )
)

lstm_model.add(Dense(1, activation="sigmoid"))

lstm_model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history_lstm = lstm_model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    validation_data=(X_test, y_test),
    verbose=1
)

loss, lstm_accuracy = lstm_model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("LSTM Accuracy :", round(lstm_accuracy * 100,2), "%")

# -------------------------------------------------
# GRU Model

gru_model = Sequential()

gru_model.add(
    GRU(
        32,
        input_shape=(X_train.shape[1], X_train.shape[2])
    )
)

gru_model.add(Dense(1, activation="sigmoid"))

gru_model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

history_gru = gru_model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=8,
    validation_data=(X_test, y_test),
    verbose=1
)

loss, gru_accuracy = gru_model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("GRU Accuracy :", round(gru_accuracy * 100,2), "%")

comparison = pd.DataFrame({

    "Model":[
        "Simple RNN",
        "LSTM",
        "GRU"
    ],

    "Accuracy":[
        accuracy,
        lstm_accuracy,
        gru_accuracy
    ]

})

print(comparison)

plt.figure(figsize=(7,4))

sns.barplot(
    data=comparison,
    x="Model",
    y="Accuracy"
)

plt.title("Deep Learning Model Comparison")

plt.show()


plt.figure(figsize=(10,5))

plt.plot(history_rnn.history["loss"], label="RNN")

plt.plot(history_lstm.history["loss"], label="LSTM")

plt.plot(history_gru.history["loss"], label="GRU")

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("Training Loss Comparison")

plt.legend()

plt.grid(True)

plt.show()

# Predict-----------------------------

prediction = gru_model.predict(X_test)

prediction = (prediction > 0.5).astype(int)

result = pd.DataFrame({

    "Actual": y_test,

    "Predicted": prediction.flatten()

})

print(result.head(10))

#     Save---------------------

result.to_csv(
    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\Task4_Predictions_spacex_launches.csv",
    index=False
)

print("Prediction file saved successfully.")