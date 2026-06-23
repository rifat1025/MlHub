import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

# dependents: int
#     tenure: int
#     online_security: int
#     online_backup: int
#     device_protection: int
#     tech_support: int
#     contract: int
#     paperless_billing: int
#     monthly_charges: float
#     total_charges: float

st.set_page_config(page_title="House Price Prediction", page_icon = "🏠")
st.title("House Price Prediction App")
st.write("Enter the details of the house to predict its price ")

dependents = st.selectbox("Dependents", options = [0,1,2,3])
tenure = st.number_input("tenure_months", min_value= 0, max_value =100)
online_security = st.selectbox("Online Security", options = [0,1])
online_backup = st.selectbox("Online Backup", options = [0,1])
device_protection = st.selectbox("Device Protection", options = [0,1])
tech_support = st.selectbox("Tech Support", options = [0,1])
contract = st.selectbox("Contract", options = [0,1,2])
paperless_billing = st.selectbox("Paperless Billing", options = [0,1])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

if st.button("Prdict Churn"):
    input_data ={
        "dependents": dependents,
        "tenure": tenure,
        "online_security": online_security,
        "online_backup": online_backup,
        "device_protection": device_protection,
        "tech_support": tech_support,
        "contract": contract,
        "paperless_billing": paperless_billing,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges
    }
    
    try:
        response = requests.post(API_URL, json = input_data, timeout = 10)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            
            if prediction == 1:
                st.error("the customer is likely to churn")
                
            else:
                st.success("the customer is not likely to churn ")
            st.json(result)
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error(f"Connection Error: {e}")
            
            
