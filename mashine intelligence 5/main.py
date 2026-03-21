import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score


iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

print("Перші 5 рядків:")
print(data.head())

print("\nІнформація про дані:")
print(data.info())

print("\nОпис статистики:")
print(data.describe())



scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)



wcss = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Кількість кластерів")
plt.ylabel("WCSS")
plt.show()



kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
k_labels = kmeans.fit_predict(scaled_data)

print("\nSilhouette Score K-means:", silhouette_score(scaled_data, k_labels))



linked = linkage(scaled_data, method='ward')

plt.figure(figsize=(10,5))
dendrogram(linked)
plt.title("Дендрограма")
plt.xlabel("Об'єкти")
plt.ylabel("Відстань")
plt.show()



dbscan = DBSCAN(eps=0.9, min_samples=5)
db_labels = dbscan.fit_predict(scaled_data)

print("\nКластери DBSCAN:", set(db_labels))
print("Кількість шумових точок:", list(db_labels).count(-1))

if len(set(db_labels)) > 1 and -1 not in set(db_labels):
    print("Silhouette Score DBSCAN:", silhouette_score(scaled_data, db_labels))
else:
    print("Silhouette Score не можна обчислити (є шум або 1 кластер)")



plt.scatter(scaled_data[:,0], scaled_data[:,1], c=k_labels)
plt.title("K-means кластеризація")
plt.show()

plt.scatter(scaled_data[:,0], scaled_data[:,1], c=db_labels)
plt.title("DBSCAN кластеризація")
plt.show()
