import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('My first app')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # file Upload box
    df = pd.read_csv(uploaded_file)

    # Display the csv file data
    st.subheader('Raw data')
    st.write(df.head())
    
    # Data Summary
    st.subheader('Data Summary')
    st.write(df.describe())

    # Data Filter
    st.subheader('Data FIlter')
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select columns to display", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("select value", unique_values)

    # # displaying filtered data
    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    # Data Plot
    st.subheader("Plot Data")
    x_colums = st.selectbox("Select x-axis column", columns)
    y_colums = st.selectbox("Select y-axis column", columns)

    
    # Generating Chart Button
    if st.button("Generate Chart"):
        st.line_chart(filtered_df.set_index(x_colums)[y_colums])
else:
    st.write("Waiting on file upload...")
