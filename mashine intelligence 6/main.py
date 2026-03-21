import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# ====================================
# 1. Генерація набору даних
# ====================================

np.random.seed(42)

# Симуляція температурної системи
# Вхід: потужність охолодження
# Вихід: температура

power = np.random.uniform(0, 100, 500)  # керуючий сигнал
temperature = 80 - 0.5 * power + np.random.normal(0, 2, 500)

X = power.reshape(-1,1)
y = temperature.reshape(-1,1)



scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42
)



model = keras.Sequential([
    layers.Dense(16, activation="relu", input_shape=(1,)),
    layers.Dense(16, activation="relu"),
    layers.Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

model.summary()



history = model.fit(
    X_train, y_train,
    epochs=100,
    validation_split=0.2,
    verbose=1
)



loss, mae = model.evaluate(X_test, y_test)
print("\nMAE:", mae)




target_temp = 30


test_powers = np.linspace(0,100,500).reshape(-1,1)
test_scaled = scaler_X.transform(test_powers)

preds = model.predict(test_scaled)
preds_real = scaler_y.inverse_transform(preds)

best_power = test_powers[np.argmin(np.abs(preds_real - target_temp))][0]

print("\nНеобхідна потужність для досягнення 30°C:", best_power)



plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Val Loss")
plt.legend()
plt.title("Графік навчання")
plt.show()



plt.scatter(power, temperature, alpha=0.4, label="Дані")
plt.plot(test_powers, preds_real, color="red", label="Модель")
plt.axhline(target_temp, linestyle="--", label="Ціль")
plt.legend()
plt.title("Керування температурою")
plt.show()