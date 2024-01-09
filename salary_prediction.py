import streamlit as st
import joblib

st.title('SALARY PREDICTION')
st.write('Using Simple Linear Regression')

test = st.number_input('Years of Experience')
if(st.button('Predict Salary')):
    model = joblib.load('dumped_model.joblib','r')
    st.success(float(model.predict([[test]])))

