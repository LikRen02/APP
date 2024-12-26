import streamlit as st
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import pickle

# Load the trained model (Save the trained XGBoost model as 'xgboost_model.pkl' before running this app)
# Uncomment below line to save model if not done:
# pickle.dump(xgb_model, open('xgboost_model.pkl', 'wb'))

model = pickle.load(open('xgboost_model.pkl', 'rb'))

# Function for prediction
def predict_fraud(data):
    # Prepare the input data (same preprocessing as training)
    data = pd.get_dummies(data, drop_first=True)
    # Ensure all columns match the training data
    all_features = X_train.columns
    missing_cols = set(all_features) - set(data.columns)
    for col in missing_cols:
        data[col] = 0
    data = data[all_features]
    prediction = model.predict(data)
    return "Fraudulent" if prediction[0] == 1 else "Not Fraudulent"

# Streamlit App Layout
st.title("E-Commerce Fraud Detection App")
st.write("Input transaction details below:")

# Input Fields
transaction_amount = st.number_input("Transaction Amount", min_value=0.0, step=0.01)
customer_age = st.number_input("Customer Age", min_value=0, step=1)
payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "PayPal", "Other"])
device_used = st.selectbox("Device Used", ["Desktop", "Mobile", "Tablet", "Other"])
transaction_day = st.slider("Transaction Day", min_value=1, max_value=31)
transaction_dow = st.slider("Transaction Day of Week (0=Monday, 6=Sunday)", min_value=0, max_value=6)
transaction_month = st.slider("Transaction Month", min_value=1, max_value=12)
is_address_match = st.selectbox("Does Shipping Address Match Billing Address?", ["Yes", "No"])

# Process inputs
input_data = pd.DataFrame({
    "Transaction Amount": [transaction_amount],
    "Customer Age": [customer_age],
    "Payment Method": [payment_method],
    "Device Used": [device_used],
    "Transaction Day": [transaction_day],
    "Transaction DOW": [transaction_dow],
    "Transaction Month": [transaction_month],
    "Is Address Match": [1 if is_address_match == "Yes" else 0]
})

# Predict button
if st.button("Predict"):
    result = predict_fraud(input_data)
    st.write(f"The transaction is predicted to be: **{result}**")