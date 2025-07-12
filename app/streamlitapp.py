import streamlit as st
import pandas as pd
from predicty import predictbind  

def main():
    # Set the title of the Streamlit app
    st.title("Predict New Medicines Using DNA Encoded Libraries")

    # Allow users to upload a CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the uploaded file
        st.write("Uploaded CSV Data:")
        st.dataframe(df)
        
        # Call the prediction function from predict.py
        try:
            prediction_result = predictbind(df)  
            st.write("Prediction Results:")
            st.dataframe(prediction_result)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    main()
