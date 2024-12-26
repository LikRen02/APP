import streamlit as st
import pickle

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