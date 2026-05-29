import pandas as pd
# from scripts.utils.logger import log_etl_run (this is professional code and run with [python -m scripts.transformation.clean_products])
import sys
import os
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from utils.logger import log_etl_run

# Read Raw Products Data
df = pd.read_csv("data/raw/products_raw.csv")

print("Raw Data Shape:", df.shape)

# Remove Duplicate Records
df = df.drop_duplicates()


# Handle Missing Values

# Numeric columns
numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Text columns
text_cols = df.select_dtypes(include=['object', 'string']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")


# Standardize Column Names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Data Type Fixes

# Convert price columns to float
if 'price' in df.columns:
    df['price'] = df['price'].astype(float)

# Convert stock to integer
if 'stock' in df.columns:
    df['stock'] = df['stock'].astype(int)


# Business Transformations

# Create discounted price column
if 'price' in df.columns and 'discountpercentage' in df.columns:

    df['discounted_price'] = (
        df['price']
        - (
            df['price']
            * df['discountpercentage']
            / 100
        )
    )

# Round discounted price
df['discounted_price'] = df['discounted_price'].round(2)

# Create stock status column
if 'stock' in df.columns:

    df['stock_status'] = df['stock'].apply(
        lambda x: 'Low Stock' if x < 20 else 'Available'
    )

# Select Important Columns

selected_columns = [
    'id',
    'title',
    'category',
    'brand',
    'price',
    'discountpercentage',
    'discounted_price',
    'rating',
    'stock',
    'stock_status'
]

df = df[selected_columns]


# Save Cleaned Data
output_path = "data/processed/products_cleaned.csv"

df.to_csv(output_path, index=False)

print("Cleaned products data saved successfully!")
print("Final Data Shape:", df.shape)

print(df.head())

log_etl_run(
    pipeline_name="Products_Transformation",
    records_processed=len(df),
    status="SUCCESS"
)