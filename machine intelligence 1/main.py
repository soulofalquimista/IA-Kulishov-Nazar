import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Створення DataFrame на основі власного набору даних
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [25000, 15000, 12000, 8000, 1500],
    "Quantity_Sold": [15, 30, 20, 10, 50]
}

df = pd.DataFrame(data)

print("=== DataFrame ===")
print(df)

#Обчислення середніх, мінімальних та максимальних значень
print("\n=== Статистика ===")
print("Середня ціна:", df["Price"].mean())
print("Мінімальна ціна:", df["Price"].min())
print("Максимальна ціна:", df["Price"].max())

print("Середня кількість продажів:", df["Quantity_Sold"].mean())
print("Мінімальна кількість продажів:", df["Quantity_Sold"].min())
print("Максимальна кількість продажів:", df["Quantity_Sold"].max())

#Побудова графіка для порівняння двох параметрів
plt.figure()
plt.plot(df["Product"], df["Price"])
plt.title("Ціна товарів")
plt.xlabel("Товар")
plt.ylabel("Ціна")
plt.show()

#Використання NumPy для математичних операцій
prices_array = np.array(df["Price"])

print("\n=== NumPy операції ===")
print("Сума цін:", np.sum(prices_array))
print("Стандартне відхилення:", np.std(prices_array))
print("Ціни зі знижкою 10%:", prices_array * 0.9)
