# main.py
import pandas as pd
from scripts.data_preprocessing import load_data, handle_missing_values, drop_unnecessary_columns
from scripts.feature_engineering import create_features, scale_features
from scripts.clustering import plot_elbow_curve, apply_kmeans, plot_pca, plot_feature_by_cluster

# Step 1: Load and preprocess data
data_path = 'data/credit_card_data.csv'
df = load_data(data_path)
df = handle_missing_values(df)
df = drop_unnecessary_columns(df)

# Step 2: Feature engineering and scaling
df = create_features(df)
df_scaled = scale_features(df)

# Step 3: Clustering and visualization
plot_elbow_curve(df_scaled)
clusters = apply_kmeans(df_scaled, n_clusters=4)
plot_pca(df_scaled, clusters)

# Step 4: Add clusters and save output
df['Cluster'] = clusters
df.to_csv('outputs/clustered_customers.csv', index=False)

# Step 5: Save feature-wise cluster boxplots
features_to_plot = ['BALANCE', 'PURCHASES', 'CREDIT_LIMIT', 'PAYMENTS', 'Total_Spend']
plot_feature_by_cluster(df, features_to_plot)

print("Pipeline executed successfully! Clustered data saved to outputs/clustered_customers.csv")