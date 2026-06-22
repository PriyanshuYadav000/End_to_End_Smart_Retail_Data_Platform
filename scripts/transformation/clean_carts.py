import pandas as pd
from scripts.utils.logger import log_etl_run


df = pd.read_csv("data/raw/carts_raw.csv")

print("Raw Carts Shape:", df.shape)


df = df.drop_duplicates()


numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


print(df.columns.tolist())


selected_columns = [
    'id',
    'userid',
    'total',
    'discountedtotal',
    'totalproducts',
    'totalquantity'
]

df = df[selected_columns]


df.to_csv("data/processed/carts_cleaned.csv", index=False)