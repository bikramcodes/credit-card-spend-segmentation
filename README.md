# 💳 Credit Card Spend Analysis & Customer Segmentation

This project analyzes customer credit card usage patterns and segments users based on their financial behavior. It simulates how a company like American Express might use transaction data to develop targeted marketing strategies, improve customer retention, and minimize risk.

---

## 🔍 Project Objective

- Understand how customers use their credit cards: spending patterns, balances, and payments.
- Segment customers into meaningful groups using unsupervised learning (K-Means).
- Provide actionable business insights and marketing recommendations for each segment.
- Build visual dashboards and reports to support data-driven decision-making.

---

## 🧰 Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- Jupyter Notebook (VS Code)
- Power BI / Tableau (for dashboarding)
- Unsupervised Learning (K-Means Clustering)
- PCA, Elbow Method, Silhouette Score

---

## 📊 Dataset

- Source: [Kaggle – Credit Card Dataset](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)
- ~9,000 customers × 18 features
- Features include balance, purchases, credit limit, payments, and more
- Preprocessed: missing value imputation, feature scaling (StandardScaler)

---

## 🧠 Segmentation Insights

| Cluster | Description | Action |
|--------|-------------|--------|
| 🏦 **High Balance Holders** | Maintain large balances but low transaction frequency | Offer premium financial products |
| 🛍️ **Frequent Spenders** | Highest purchase frequency and engagement | Loyalty offers, cashback, personalized rewards |
| 📊 **Balanced Users** | Moderate usage and stable behavior | Monitor for retention and upselling |
| 😴 **Dormant Users** | Inactive, low purchases | Re-engagement campaigns |
| 💳 **Revolvers** | Carry balances with low payments | Risk mitigation strategies, EMI offers |

---

## 📈 Key Visuals

- Correlation heatmaps to study feature relationships
- PCA for visualizing high-dimensional clusters
- Elbow + Silhouette plots for cluster optimization
- Cluster-wise comparisons of spend, balance, payments

---

## 📊 Dashboard Overview *(in `app/` folder)*

- Customer segmentation summary
- Interactive filters for cluster-wise drill-down
- KPIs and trends to support marketing strategy

---


