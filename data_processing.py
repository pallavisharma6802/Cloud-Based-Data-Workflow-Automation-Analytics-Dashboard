import pandas as pd
import boto3
from io import StringIO

# AWS S3 Configuration - Add your bucket and region
AWS_BUCKET_NAME = "<s3-bucket-name>"
AWS_REGION = "<aws-region>"

# Initialize S3 client
s3 = boto3.client(
    "s3",
    region_name=AWS_REGION
)

def load_data_from_s3(file_key):
    """Fetch data from AWS S3."""
    try:
        response = s3.get_object(Bucket=AWS_BUCKET_NAME, Key=file_key)
        data = response['Body'].read().decode('utf-8')
        return pd.read_csv(StringIO(data))
    except Exception as e:
        print(f"Error loading data from S3: {e}")
        return None

def load_data_from_google_drive(link):
    """Fetch CSV file from Google Drive (public link)."""
    try:
        file_id = link.split("/d/")[1].split("/")[0]
        raw_url = f"https://drive.google.com/uc?id={file_id}"
        return pd.read_csv(raw_url)
    except Exception as e:
        print(f"Error loading data from Google Drive: {e}")
        return None

def preprocess_data(df):
    """Basic data cleaning & formatting."""
    if df is None or df.empty:
        return None
    
    df.dropna(inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Convert object columns to numeric where possible
    for col in df.select_dtypes(include=['object']):
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except:
            pass

    return df
