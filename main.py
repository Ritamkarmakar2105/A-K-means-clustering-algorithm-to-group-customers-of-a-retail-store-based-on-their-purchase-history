import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Loading the dataset
data = pd.read_csv(r"D:\mall customer segmentation\Mall_Customers.csv")

# Selecting features for clustering: Annual Income and Spending Score
X = data[['Annual Income (k$)', 'Spending Score (1-100)']].values

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determining the optimal number of clusters using the elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plotting the elbow curve
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.savefig('elbow_curve.png')
plt.close()

# Applying K-means clustering with 5 clusters (based on elbow method observation)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Adding cluster labels to the original dataset
data['Cluster'] = clusters

# Visualizing the clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', s=100)
plt.scatter(kmeans.cluster_centers_[:, 0] * scaler.scale_[0] + scaler.mean_[0], 
            kmeans.cluster_centers_[:, 1] * scaler.scale_[1] + scaler.mean_[1], 
            s=300, c='red', marker='*', label='Centroids')
plt.title('Customer Segments based on Annual Income and Spending Score')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend(handles=scatter.legend_elements()[0], 
          labels=['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4'])
plt.savefig('customer_clusters.png')
plt.close()

# Saving the dataset with cluster labels
data.to_csv('Mall_Customers_Clustered.csv', index=False)

# Printing cluster characteristics
print("Cluster Characteristics:")
for i in range(5):
    cluster_data = data[data['Cluster'] == i]
    print(f"\nCluster {i}:")
    print(f"Number of customers: {len(cluster_data)}")
    print(f"Average Annual Income: ${cluster_data['Annual Income (k$)'].mean():.2f}k")
    print(f"Average Spending Score: {cluster_data['Spending Score (1-100)'].mean():.2f}")