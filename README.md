# 🥑 Avocado Price Prediction

An end-to-end data science and machine learning project focused on analyzing historical avocado sales data and predicting average avocado prices using regression models.

---

## 📌 Project Overview

The goal of this project is to explore real-world avocado sales data, perform exploratory data analysis (EDA), and build regression models to predict the **average price of avocados** across different regions and time periods.

This project demonstrates the complete data science workflow:
- Data cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- Regression modeling
- Model evaluation

---

## 📂 Dataset

- **Source:** Avocado sales dataset
- **Records:** ~18,000+
- **Target Variable:** `AveragePrice`

### Key Features:
- Total Volume
- Avocado size-wise sales (4046, 4225, 4770)
- Bag sizes (Small, Large, XLarge)
- Type (Conventional / Organic)
- Region
- Date (converted into year and month)

---

## 🔍 Exploratory Data Analysis (EDA)

- Price trends over time
- Comparison between organic and conventional avocado prices
- Region-wise pricing behavior
- Distribution analysis of prices and volumes
- Correlation analysis between numerical features

---

## 🛠️ Feature Engineering

- Converted date column into `year` and `month`
- Encoded categorical variables (`type`, `region`) using one-hot encoding
- Handled missing values using mean imputation
- Prepared data for regression modeling

---

## 🤖 Machine Learning Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Model comparison based on R² score and error metrics

---

## 📊 Model Evaluation

- R² Score
- Mean Squared Error (MSE)
- Comparison of multiple regression models to select the best-performing model

---

## 🧰 Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Jupyter Notebook

---

## 📁 Project Structure
