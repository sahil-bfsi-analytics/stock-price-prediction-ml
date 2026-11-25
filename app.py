import streamlit as st
import pandas as pd
import pickle

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Stock Price Predictor",
    page_icon="📈",
    layout="centered"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

/* Main Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 17px;
    margin-bottom: 30px;
}

/* Input Card */
.input-card {
    background-color: white;
    padding: 25px 30px;
    border-radius: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* Prediction Card */
.prediction-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.10);
    margin-top: 25px;
}

.prediction-label {
    font-size: 18px;
    color: #6b7280;
}

.prediction-value {
    font-size: 42px;
    font-weight: 700;
    margin-top: 8px;
}

/* Button */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 17px;
    font-weight: 600;
}

/* Section Heading */
.section-title {
    font-size: 22px;
    font-weight: 650;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 13px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL AND SCALER
# ============================================================

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">📈 Stock Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict the stock closing price using Linear Regression'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# INPUT CARD
# ============================================================

st.markdown(
    '<div class="input-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">📊 Stock Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    High = st.number_input(
        "High",
        min_value=0.0,
        value=502.50,
        step=0.01
    )

    Low = st.number_input(
        "Low",
        min_value=0.0,
        value=495.35,
        step=0.01
    )

    Open = st.number_input(
        "Open",
        min_value=0.0,
        value=500.00,
        step=0.01
    )

    MA_7 = st.number_input(
        "MA_7",
        min_value=0.0,
        value=505.36,
        step=0.01
    )

    MA_30 = st.number_input(
        "MA_30",
        min_value=0.0,
        value=512.68,
        step=0.01
    )


with col2:

    NSE_Symbol_TATASTEEL = st.selectbox(
        "NSE Symbol - TATASTEEL",
        [0, 1]
    )

    NSE_Symbol_TATAPOWER = st.selectbox(
        "NSE Symbol - TATAPOWER",
        [0, 1]
    )

    Daily_Return = st.number_input(
        "Daily Return",
        value=0.004580,
        step=0.000001,
        format="%.6f"
    )

    Market_Cap = st.number_input(
        "Market Cap (Current, INR Cr)",
        min_value=0.0,
        value=459674.8819,
        step=100.0
    )

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("🚀 Predict Close Price"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        'High': [High],
        'Low': [Low],
        'Open': [Open],
        'MA_7': [MA_7],
        'MA_30': [MA_30],
        'NSE Symbol_TATASTEEL': [NSE_Symbol_TATASTEEL],
        'NSE Symbol_TATAPOWER': [NSE_Symbol_TATAPOWER],
        'Daily Return': [Daily_Return],
        'Market Cap (Current, INR Cr)': [Market_Cap]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    predicted_price = prediction[0]

    # Display result
    st.markdown(
        f"""
        <div class="prediction-card">
            <div class="prediction-label">
                Predicted Closing Price
            </div>
            <div class="prediction-value">
                ₹{predicted_price:,.2f}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    'Machine Learning Model • Linear Regression • Stock Price Prediction'
    '</div>',
    unsafe_allow_html=True
)