
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('chrun_prediction.pkl')

# def main_page():
st.title('Churn Customer Prediction')
gender = st.radio(label='Gender',options=['Female','Male'])
age = st.number_input(label='Enter Customer Age: ')
if age >= 60:
    senior = 1
else:
    senior = 0 

partner = st.radio(label='Partner',options=['Yes','No'])
dependents = st.selectbox(label='Dependents',options=['Yes','No'])
tenure = st.number_input(label='Tenure in months')
phone_service = st.radio(label='Phone Service',options=['Yes','No'])
multiple_lines = st.selectbox(label='MultipleLines',options=['Yes','No','No phone service'])
internet_service = st.selectbox(label='Internet Service',options=['DSL','Fiber optic','No'])
online_security = st.selectbox(label='Online Security',options=['Yes','No','No internet service'])
online_backup = st.selectbox(label='Online Backup',options=['Yes','No','No internet service'])
device_protection = st.selectbox(label='Device Protection',options=['Yes','No','No internet service'])
tech_support = st.selectbox(label='Tech Support',options=['Yes','No','No internet service'])
streaming_tv =st.selectbox(label='Streaming TV',options=['Yes','No','No internet service'])
streaming_movies = st.selectbox(label='Streaming Movies',options=['Yes','No','No internet service'])
contract = st.selectbox(label='Contract',options=['One year','Month-to-month','Two year'])
paperless_billing = st.radio(label='Paperless Billing',options=['Yes','No'])
payment_method = st.selectbox(label='Payment Method',options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.number_input(label='Monthly Charges')
total_charges = st.number_input(label='Total Charges')

if monthly_charges > 0 :
    completed_service = tenure - (total_charges / monthly_charges)
else:
    completed_service = 0  

if completed_service >= 1:
    completedservice = 1
else:
    completedservice = 0         


input_data = pd.DataFrame(
    {
        'gender':[gender],
        'seniorcitizen':[senior],
        'partner':[partner],
        'dependents':[dependents],
        'tenure':[tenure], 
        'phoneservice':[phone_service],
        'multiplelines':[multiple_lines], 
        'internetservice':[internet_service],
        'onlinesecurity':[online_security],
        'onlinebackup':[online_backup],
        'deviceprotection':[device_protection],
        'techsupport':[tech_support],
        'streamingtv':[streaming_tv], 
        'streamingmovies':[streaming_movies],
        'contract':[contract],
        'paperlessbilling':[paperless_billing],
        'paymentmethod':[payment_method], 
        'monthlycharges':[monthly_charges],
        'totalcharges':[total_charges],
        'completedservice':[completedservice]
    }
)

if st.button(label='Predict'):
    prediction = model.predict(input_data)
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is likely to stay.")

with st.expander("Customer Input Summary"):
        st.dataframe(input_data)    
