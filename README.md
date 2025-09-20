
#Cloud-Based Data Analytics Dashboard

## Overview
**Cloud-Based Data Analytics Dashboard** is an interactive application built with **Streamlit** that enables users to upload datasets from **AWS S3**, **Google Drive**, or local CSV files.  
The platform automates data preprocessing, stores data in a local **SQLite** database, and offers dynamic visualizations along with a real-time **SQL query interface** for flexible data exploration and reporting.

---

## Key Features
- **Cloud and Local Data Ingestion**:  
  Upload datasets directly from AWS S3, Google Drive links, or local CSV files.
  
- **Automated Data Preprocessing**:  
  Standardizes, cleans, and formats uploaded datasets automatically.

- **Local Data Storage**:  
  Saves processed datasets into a SQLite database for efficient querying and retrieval.

- **Interactive Visualizations**:  
  Generate category-wise bar plots and time-series analyses using Matplotlib.

- **Real-Time SQL Query Execution**:  
  Run custom SQL queries on the stored datasets through the dashboard interface.

- **Modular Architecture**:  
  Separate modules for data loading, preprocessing, storage, and analytics to support easy extension.

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: SQLite
- **Cloud Integration**: AWS S3, Google Drive
- **Data Processing**: Pandas
- **Visualization**: Matplotlib

---

## How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/pallavisharma6802/Cloud-Based-Data-Workflow-Automation-Analytics-Dashboard.git
   ```

3. **Launch the application**
   ```bash
   streamlit run app.py
   ```

---

## Dataset Requirements
Uploaded CSV files should contain at minimum the following columns (flexible after preprocessing):
- **Date** (in any consistent format)
- **Category** (categorical variable for grouping)
- **Value** (numeric measurement for analysis)

