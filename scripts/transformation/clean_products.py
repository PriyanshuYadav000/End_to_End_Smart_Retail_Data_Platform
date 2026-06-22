import pandas as pd

import sys
import os
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
from utils.logger import log_etl_run


df = pd.read_csv("data/raw/products_raw.csv")

print("Raw Data Shape:", df.shape)


df = df.drop_duplicates()



numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())


text_cols = df.select_dtypes(include=['object', 'string']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")



df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


if 'price' in df.columns:
    df['price'] = df['price'].astype(float)


if 'stock' in df.columns:
    df['stock'] = df['stock'].astype(int)



if 'price' in df.columns and 'discountpercentage' in df.columns:

    df['discounted_price'] = (
        df['price']
        - (
            df['price']
            * df['discountpercentage']
            / 100
        )
    )


df['discounted_price'] = df['discounted_price'].round(2)


if 'stock' in df.columns:

    df['stock_status'] = df['stock'].apply(
        lambda x: 'Low Stock' if x < 20 else 'Available'
    )



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