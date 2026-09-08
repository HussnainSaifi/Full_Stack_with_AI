# Section B - Task 3
# Deep Learning using RNN, LSTM and GRU
# Dataset : spacex.csv

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

df = pd.read_csv(r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\datasets\spacex.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

print(df.select_dtypes(include=np.number).columns)

# ------------------------------------------
# Convert Date Column

df["Datetime"] = pd.to_datetime(df["Datetime"])

df = df.sort_values("Datetime")

df.reset_index(drop=True, inplace=True)


# -------------------------------------------------
# Select Close Price

data = df[["Close"]]

print(data.head())



# -------------------------------------------
# Scale Data

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(data)

print(scaled_data[:5])


# ---------------------------------------
# Create Sequences

sequence_length = 5

X = []

y = []

for i in range(sequence_length, len(scaled_data)):

    X.append(scaled_data[i-sequence_length:i])

    y.append(scaled_data[i])

X = np.array(X)

y = np.array(y)

print(X.shape)

print(y.shape)


# ---------------------------------------
# Train Test Split

split = int(len(X) * 0.80)

X_train = X[:split]

X_test = X[split:]

y_train = y[:split]

y_test = y[split:]

print(X_train.shape)

print(X_test.shape)


# --------------------------------------
# Simple RNN Model

rnn_model = Sequential()

rnn_model.add(
    SimpleRNN(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1],1)
    )
)

rnn_model.add(Dense(1))

rnn_model.compile(

    optimizer="adam",

    loss="mse"

)

history_rnn = rnn_model.fit(

    X_train,

    y_train,

    epochs=30,

    batch_size=4,

    verbose=1
)

# ----------------------------------
# RNN Prediction

rnn_prediction = rnn_model.predict(X_test)

rnn_prediction = scaler.inverse_transform(rnn_prediction)

actual = scaler.inverse_transform(y_test)

rmse = np.sqrt(

    mean_squared_error(

        actual,

        rnn_prediction

    )

)

print("RNN RMSE :", rmse)


plt.figure(figsize=(10,5))

plt.plot(actual,label="Actual")

plt.plot(rnn_prediction,label="Predicted")

plt.title("Simple RNN Prediction")

plt.legend()

plt.show()


# -------------------------------------
# LSTM Model

lstm_model = Sequential()

lstm_model.add(
    LSTM(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1],1)
    )
)

lstm_model.add(Dense(1))

lstm_model.compile(
    optimizer="adam",
    loss="mse"
)

history_lstm = lstm_model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=4,
    verbose=1
)

lstm_prediction = lstm_model.predict(X_test)

lstm_prediction = scaler.inverse_transform(lstm_prediction)

lstm_rmse = np.sqrt(
    mean_squared_error(
        actual,
        lstm_prediction
    )
)

print("LSTM RMSE :", lstm_rmse)

# -----------------------------------
# GRU Model

gru_model = Sequential()

gru_model.add(
    GRU(
        32,
        activation="tanh",
        input_shape=(X_train.shape[1],1)
    )
)

gru_model.add(Dense(1))

gru_model.compile(
    optimizer="adam",
    loss="mse"
)

history_gru = gru_model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=4,
    verbose=1
)

gru_prediction = gru_model.predict(X_test)

gru_prediction = scaler.inverse_transform(gru_prediction)

gru_rmse = np.sqrt(
    mean_squared_error(
        actual,
        gru_prediction
    )
)

print("GRU RMSE :", gru_rmse)

results = pd.DataFrame({

    "Model":[
        "Simple RNN",
        "LSTM",
        "GRU"
    ],

    "RMSE":[
        rmse,
        lstm_rmse,
        gru_rmse
    ]

})

print(results)

#Graph

plt.figure(figsize=(7,4))

sns.barplot(
    data=results,
    x="Model",
    y="RMSE"
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


#Prediction
prediction_df = pd.DataFrame({

    "Actual":actual.flatten(),

    "RNN":rnn_prediction.flatten(),

    "LSTM":lstm_prediction.flatten(),

    "GRU":gru_prediction.flatten()

})
#Save
prediction_df.to_csv(

    r"C:\Users\Hussnain Saifi\Documents\GitHub\CLass-3\Final_Assignemnts\Task3_Predictions_spacex.csv",

    index=False

)

print(prediction_df.head())