import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import requests

# Define the API endpoint
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'

# Set the start date and end date
start_date = '2010-07-17'
end_date = dt.date.today().strftime('%Y-%m-%d')

# Make the API request
params = {'start': start_date, 'end': end_date}
response = requests.get(url, params=params)

# Convert the JSON response to a pandas DataFrame
df = pd.DataFrame.from_dict(response.json()['bpi'], orient='index', columns=['Close'])
df.index = pd.to_datetime(df.index)

# Resample the data to daily frequency
df = df.resample('D').ffill()

# Normalize the data
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df.values)

# Split the data into training and testing sets
train_size = int(len(df_scaled) * 0.8)
test_size = len(df_scaled) - train_size
train_data = df_scaled[0:train_size,:]
test_data = df_scaled[train_size:len(df_scaled),:]

# Convert the data into sequences
def create_sequences(data, seq_length):
    X = []
    y = []
    for i in range(len(data)-seq_length-1):
        X.append(data[i:(i+seq_length), 0])
        y.append(data[(i+seq_length), 0])
    return np.array(X), np.array(y)

seq_length = 30
X_train, y_train = create_sequences(train_data, seq_length)
X_test, y_test = create_sequences(test_data, seq_length)

# Define the deep learning model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(units=64, input_shape=(X_train.shape[1], 1)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32)

# Evaluate the model on the test data
loss = model.evaluate(X_test, y_test)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Inverse normalize the data
y_pred = scaler.inverse_transform(y_pred)
y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

# Plot the predicted and actual prices
plt.figure(figsize=(10, 5))
plt.plot(y_test, label='Actual Price')
plt.plot(y_pred, label='Predicted Price')
plt.title('Bitcoin Price Prediction')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.legend()

# Plot the moving average of the actual price
window_size = 7
rolling_mean = df['Close'].rolling(window=window_size).mean()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='Actual Price')
plt.plot(rolling_mean.index, rolling_mean, label='Moving Average')
plt.title('Bitcoin Price')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()


# Plot the mean squared error during training
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'])
plt.title('Model Training Performance')
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error')
plt.legend()
plt.show()

# Define the number of days to predict
num_days = 365

# Create an array to hold the predicted prices
predicted_prices = np.zeros((num_days, 1))

# Use the last sequence in the training data to start predicting
last_sequence = X_train[-1]

# Predict the prices for the next num_days days
for i in range(num_days):
    # Reshape the last_sequence to have a shape of (1, seq_length, 1)
    last_sequence = last_sequence.reshape((1, seq_length, 1))
    # Predict the next price
    next_price = model.predict(last_sequence)
    # Add the next price to the predicted_prices array
    predicted_prices[i] = next_price
    # Shift the last_sequence by one and add the next_price at the end
    last_sequence = np.roll(last_sequence, -1, axis=1)
    last_sequence[0, -1, 0] = next_price

# Inverse normalize the predicted prices
predicted_prices = scaler.inverse_transform(predicted_prices)

# Create an array of dates starting from the last date in the training data
last_date = df.index[-1]
dates = pd.date_range(last_date, periods=num_days+1, freq='D')[1:]

# Plot the predicted prices
plt.figure(figsize=(10, 5))
plt.plot(dates, predicted_prices, label='Predicted Price')
plt.title('Bitcoin Price Prediction for the Next Year')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()