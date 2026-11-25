# 📈 Stock Price Prediction using Machine Learning

An end-to-end machine learning project that predicts the **closing price** of Tata Group stocks using **Linear Regression**, with an interactive **Streamlit** web app for real-time predictions.

---

## 📌 Project Overview

This project covers the complete data science workflow: data cleaning, exploratory data analysis (EDA), statistical feature selection, model training, and deployment as a web application.

- **Dataset:** Tata Group stock data (6 companies: TCS, Tata Motors, Tata Power, Tata Steel, Tata Technologies, Tata Consumer Products; ~2,390 records after cleaning, Dec 2024 – Jul 2026)
- **Target Variable:** `Close` price
- **Model:** Linear Regression with StandardScaler
- **Deployment:** Streamlit web app

---

## 🚀 Features

- Predicts the closing price instantly from user-provided market inputs
- Uses pre-trained `model.pkl` and `scaler.pkl` for consistent preprocessing and fast inference
- Clean, interactive Streamlit UI
- Full EDA and training workflow documented in the Jupyter Notebook

---

## 🔬 Methodology

1. **Data Cleaning**
   - Checked duplicates (0 found) and removed rows with null values (2,394 → 2,390 rows)
   - Converted `Date` to datetime and `is_imputed` to integer
   - Dropped irrelevant columns: `Company Name`, `BSE Code`, `Adjusted Close`, `Sector`
2. **Exploratory Data Analysis**
   - Distribution plots, boxplots (outlier detection), time-series plots
   - Close price vs. moving averages (MA_7, MA_30)
   - Correlation heatmap
3. **Encoding**
   - One-hot encoding of `NSE Symbol` (`drop_first=True`)
4. **Feature Selection**
   - **Pearson correlation** for numeric features against `Close`
   - **Chi-Square test** (Close binned into quartiles) for categorical features
5. **Model Training**
   - 80/20 train-test split (`random_state=42`)
   - `StandardScaler` for feature scaling
   - `LinearRegression` model
   - Model and scaler saved with Pickle
6. **Deployment**
   - Streamlit app that loads the saved artifacts and predicts on user input

---

## 🎯 Final Features Used

`High`, `Low`, `Open`, `MA_7`, `MA_30`, `Daily Return`, `Market Cap (Current, INR Cr)`, `NSE Symbol_TATASTEEL`, `NSE Symbol_TATAPOWER`

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, SciPy, Matplotlib, Seaborn
- **Web Framework:** Streamlit
- **Serialization:** Pickle

---

## 📂 Project Structure

```text
stock-price-prediction-ml/
│
├── app.py                                   # Streamlit web application
├── LinearregressionProject12-08-2026.ipynb  # EDA, feature selection & model training
├── tata_group_stock_dataset.csv             # Dataset (6 Tata Group stocks)
├── model.pkl                                # Trained Linear Regression model
├── scaler.pkl                               # Fitted StandardScaler
├── requirements.txt                         # Project dependencies
└── README.md                                # Project documentation
```

---

## ⚙️ Installation & Usage

**1. Clone the repository**
```bash
git clone https://github.com/sahil-bfsi-analytics/stock-price-prediction-ml.git
cd stock-price-prediction-ml
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

> **Note:** The saved `model.pkl` and `scaler.pkl` were created with scikit-learn 1.6.1. Using the same version avoids version-mismatch warnings.

**3. Run the Streamlit app**
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 🖥️ How to Use the App

Enter the following inputs and click **Predict Close Price**:

| Input | Description |
|---|---|
| High / Low / Open | Day's price values |
| MA_7 / MA_30 | 7-day and 30-day moving averages |
| Daily Return | Day's percentage return (decimal) |
| Market Cap | Market capitalization (INR Cr) |
| NSE Symbol | 1 if TATASTEEL / TATAPOWER, else 0 |

---

## ⚠️ Limitations

- Features such as Open/High/Low are same-day values, so this model estimates the close from intraday data rather than forecasting future prices.
- A random train-test split is used; a time-based split would be more realistic for time-series data.
- This project is for learning and demonstration purposes only, **not financial advice**.

---

## 🔮 Future Improvements

- Time-based train/test split and cross-validation
- Compare with Random Forest, XGBoost, LSTM
- Add evaluation metrics dashboard (R², RMSE, MAE) in the app
- Deploy on Streamlit Community Cloud

---

## 👤 Author

**Sahil Mehta**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/sahil-mehta-a69073452)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/sahil-bfsi-analytics)