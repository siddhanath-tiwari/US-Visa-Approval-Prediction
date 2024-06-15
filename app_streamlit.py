import streamlit as st
import pandas as pd
from us_visa.entity.config_entity import USvisaPredictorConfig
from us_visa.entity.s3_estimator import USvisaEstimator
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.utils.main_utils import read_yaml_file
from pandas import DataFrame

# Import your USvisaData and USvisaClassifier classes here
from your_module import USvisaData, USvisaClassifier

# Define Streamlit app header
st.title('US Visa Approval Prediction App')

# Define input fields using Streamlit widgets
continent = st.selectbox('Select Continent', ['Asia', 'Europe', 'North America', 'South America'])
education = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
# Add more input fields as per your USvisaData class constructor parameters

# Function to create USvisaData object from user input
def create_usvisa_data_object():
    return USvisaData(
        continent=continent,
        education_of_employee=education,
        # Add remaining parameters based on your class constructor
        # Example: has_job_experience=st.checkbox('Has Job Experience'),
    )

# Function to perform prediction and display result
def predict_approval():
    try:
        # Create USvisaData object
        usvisa_data = create_usvisa_data_object()

        # Get input data as DataFrame
        input_dataframe = usvisa_data.get_usvisa_input_data_frame()

        # Create USvisaClassifier object (adjust constructor as per your implementation)
        classifier = USvisaClassifier(prediction_pipeline_config=USvisaPredictorConfig())

        # Perform prediction
        prediction_result = classifier.predict(input_dataframe)

        # Display prediction result
        st.write('Prediction Result:', prediction_result)

    except USvisaException as e:
        st.error(f'Prediction Error: {str(e)}')

# Add a button to trigger prediction
if st.button('Predict'):
    predict_approval()
