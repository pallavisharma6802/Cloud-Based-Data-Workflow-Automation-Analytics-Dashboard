import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_processing import load_data_from_s3, load_data_from_google_drive, preprocess_data
from database import save_to_db, fetch_data_from_db, execute_custom_query, close_connection

st.title("📊 Cloud-Based Data Analytics Dashboard")

# Data Source Selection
option = st.radio("Select Data Source:", ("AWS S3", "Google Drive Link", "Upload CSV"))

if option == "AWS S3":
    file_key = st.text_input("Enter S3 File Key (e.g., data/sample.csv):")
    if st.button("Load Data from S3") and file_key:
        df = load_data_from_s3(file_key)
        df = preprocess_data(df)
        if df is not None:
            save_to_db(df)
            st.success("Data Loaded and Stored Successfully!")

elif option == "Google Drive Link":
    drive_link = st.text_input("Enter Google Drive Shareable Link:")
    if st.button("Load Data from Google Drive") and drive_link:
        df = load_data_from_google_drive(drive_link)
        df = preprocess_data(df)
        if df is not None:
            save_to_db(df)
            st.success("Data Loaded and Stored Successfully!")

elif option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = preprocess_data(df)
        if df is not None:
            save_to_db(df)
            st.success("Data Uploaded and Stored Successfully!")

# Display Data
df = fetch_data_from_db()
st.subheader("📊 Processed Data")
st.write(df.head())

# Visualization - Category Distribution
st.subheader("📈 Category Distribution")
if "category" in df.columns:
    fig, ax = plt.subplots()
    df["category"].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)

# Time-Series Visualization (if date column exists)
if "date" in df.columns:
    st.subheader("📅 Time Series Analysis")
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    fig, ax = plt.subplots()
    df["value"].resample("M").sum().plot(ax=ax, title="Monthly Value Trend")
    st.pyplot(fig)

# Custom SQL Query Interface
st.subheader("🛠️ Run Custom SQL Query")
query = st.text_area("Enter SQL Query:")
if st.button("Run Query"):
    result = execute_custom_query(query)
    st.write(result)

# Close DB connection
close_connection()
