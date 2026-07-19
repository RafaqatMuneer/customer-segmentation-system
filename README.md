# 🛍️ Customer Segmentation System

An end-to-end Machine Learning application that segments customers into distinct groups using the **K-Means Clustering** algorithm. The project includes data preprocessing, model training, a Flask REST API, a Streamlit frontend, and deployment-ready structure.

---

## 📌 Project Overview

Customer segmentation helps businesses understand different customer groups based on their demographic and purchasing behavior. This project predicts the customer segment using K-Means Clustering and provides a meaningful business interpretation along with a marketing recommendation.

---

## 🎯 Objectives

- Segment customers into meaningful groups.
- Analyze customer behavior using unsupervised learning.
- Build a complete end-to-end machine learning application.
- Provide an interactive web interface for customer segmentation.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- K-Means Clustering
- OneHotEncoder
- StandardScaler
- ColumnTransformer
- Pipeline
- Joblib
- Flask
- Streamlit
- Git & GitHub

---

## 📂 Dataset Features

### Input Features

- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

### Output

- Customer Cluster
- Customer Segment
- Segment Description
- Marketing Recommendation

---

## 🤖 Machine Learning Model

**Algorithm:** K-Means Clustering

### Data Preprocessing

- Missing value handling
- One-Hot Encoding for categorical features
- Standard Scaling for numerical features
- Pipeline implementation using ColumnTransformer

### Model Evaluation

- Elbow Method
- Silhouette Score

**Selected Number of Clusters:** 5

**Silhouette Score:** 0.55

---

## 🏷️ Customer Segments

| Cluster | Segment |
|----------|------------------------------|
| 1 | Regular Customer |
| 2 | Premium Customer |
| 3 | Young Enthusiastic Shopper |
| 4 | High Income Saver |
| 5 | Budget Customer |

---

## 🌐 Application Architecture

```text
                Streamlit Frontend
                       │
                       ▼
               Flask REST API
                       │
                       ▼
         Trained K-Means Pipeline (.joblib)
                       │
                       ▼
             Customer Segment Prediction
```

---

## 🚀 Running the Project Locally

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project

```bash
cd Customer_Segmentation_System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask API

```bash
python app.py
```

### 5. Run the Streamlit Frontend

```bash
streamlit run streamlit_app/app.py
```

---

## 📁 Project Structure

```text
Customer_Segmentation_System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── customer_segmentation.joblib
│
├── streamlit_app/
│   └── app.py
│
├── dataset/
│
└── notebooks/
```

---

## 📡 API Endpoint

### POST `/predict`

### Sample Request

```json
{
  "Gender": "Female",
  "Age": 29,
  "Annual Income (k$)": 82,
  "Spending Score (1-100)": 88
}
```

### Sample Response

```json
{
  "cluster": 2,
  "segment": "Premium Customer",
  "description": "High-income customers who spend frequently and are ideal for premium offers.",
  "marketing_action": "Offer premium memberships and exclusive promotions."
}
```

---

## ☁️ Deployment

### Flask API

Deploy the Flask API to a cloud platform such as:

- Render
- Railway
- Fly.io

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn app:app
```

---

### Streamlit Frontend

Deploy the frontend using **Streamlit Community Cloud**.

After deploying the Flask API, replace the local API URL:

```python
http://127.0.0.1:5000/predict
```

with your deployed API URL:

```python
https://your-api-url.onrender.com/predict
```

Then deploy the Streamlit application by selecting:

```text
streamlit_app/app.py
```

as the main file.

---

## 📈 Future Improvements

- Customer profile visualization
- Interactive cluster plots
- Business analytics dashboard
- Download prediction reports
- Customer history management
- Advanced marketing insights

---

## 👨‍💻 Author : Rafaqat Muneer

Developed as an end-to-end Machine Learning project demonstrating data preprocessing, clustering, REST API development, frontend integration, and cloud deployment using Python.