import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns
import pandas as pd


def plot_elbow_curve(data, max_k=10):
    inertia = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia.append(kmeans.inertia_)

    plt.plot(range(1, max_k + 1), inertia, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method For Optimal k')
    plt.savefig(f'images/elbow_curve.png')
    plt.show()

def apply_kmeans(data, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    return clusters

def plot_pca(data, clusters):
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(data)
    
    plt.figure()
    sns.scatterplot(x=reduced[:, 0], y=reduced[:, 1], hue=clusters, palette='viridis')
    plt.title('PCA Clusters')
    plt.savefig(f'images/pca_clusters.png')
    plt.show()


def plot_feature_by_cluster(df, features):
    for feature in features:
        plt.figure()
        sns.boxplot(x='Cluster', y=feature, data=df)
        plt.title(f'{feature} by Cluster')
        plt.savefig(f'images/cluster_{feature}_boxplot.png')
        plt.close()
