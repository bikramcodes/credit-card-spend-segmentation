# Credit Card Spend Segmentation

An Amex-level customer segmentation project using unsupervised learning to group credit card users based on spending behavior. The goal is to identify user personas and derive business strategies tailored to each segment.

---

## 📌 Objective

To segment customers based on transactional behavior to:

- Design personalized marketing offers
- Reduce churn and improve credit utilization
- Optimize credit limit allocation

---

## 🧾 Dataset

**Source:** [Kaggle - Credit Card Dataset for Clustering](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata)

**Rows:** 8950

**Columns:**

- BALANCE, PURCHASES, ONEOFF\_PURCHASES, CASH\_ADVANCE
- CREDIT\_LIMIT, PAYMENTS, MINIMUM\_PAYMENTS
- PURCHASES\_FREQUENCY, PRC\_FULL\_PAYMENT, TENURE

---

## 🧪 Steps Performed

### 1. **Data Preprocessing**

- Handled missing values (e.g., CREDIT\_LIMIT, MINIMUM\_PAYMENTS)
- Dropped `CUST_ID` (non-numeric)

### 2. **Feature Engineering**

- `Total_Spend = PURCHASES + CASH_ADVANCE`
- `Payment_to_MinPay = PAYMENTS / MINIMUM_PAYMENTS`
- `Balance_Limit_Ratio = BALANCE / CREDIT_LIMIT`

### 3. **Feature Scaling**

Used `StandardScaler` to normalize features

### 4. **Dimensionality Reduction**

PCA was used for visualizing data in 2D space

### 5. **Clustering (KMeans)**

- Elbow method used to select optimal k
- Final clustering done using `k=4`

### 6. **Cluster Profiling & Visualization**

- Mean values calculated for each cluster
- Visualizations plotted for: BALANCE, PURCHASES, CREDIT\_LIMIT, etc.

---

## 📊 Cluster Insights

| Cluster | Traits                                           | Suggested Strategy                              |
| ------- | ------------------------------------------------ | ----------------------------------------------- |
| **0**   | High balance, high spenders, high limits         | Offer premium rewards, loyalty upgrades         |
| **1**   | Low spend, minimal transactions, moderate credit | Dormant reactivation via cashback or EMI offers |
| **2**   | Moderate use, full payers, small purchases       | Upsell mid-tier benefits, encourage more usage  |
| **3**   | Very low activity, zero balance/usage            | Target for exit or re-engagement campaigns      |

---

## 📁 Folder Structure

```
credit-card-spend-segmentation/
├── data/
├── notebooks/
│   └── 01_data_analysis.ipynb
├── scripts/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── clustering.py
├── images/
│   ├── elbow_curve.png
│   ├── pca_clusters.png
│   ├── cluster_BALANCE_boxplot.png
├── outputs/
│   └── clustered_customers.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python, Pandas, NumPy
- Scikit-learn, Matplotlib, Seaborn
- Jupyter Notebook

---

## 📈 Key Visuals

- Elbow Method (images/elbow\_curve.png)
- PCA Projection (images/pca\_clusters.png)
- Clustered Boxplots (e.g. BALANCE, PURCHASES)

---

## ✅ Results

- Successfully segmented customers into 4 distinct groups
- Developed actionable business recommendations
- All code modularized for production pipeline

---

## 🔗 Author

**Bikram Singh**\
Data Analyst | ML Enthusiast | Portfolio Builder

---

