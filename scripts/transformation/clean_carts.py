import pandas as pd
from scripts.utils.logger import log_etl_run

# Read raw carts data
df = pd.read_csv("data/raw/carts_raw.csv")

print("Raw Carts Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Standardize columns
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Select important columns
selected_columns = [
    'id',
    'userid',
    'total',
    'discountedtotal',
    'totalproducts',
    'totalquantity'
]

df = df[selected_columns]

# Save cleaned carts data
df.to_csv("data/processed/carts_cleaned.csv", index=False)

print("Carts cleaned successfully!")
print(df.head())

log_etl_run(
    pipeline_name="Carts_Transformation",
    records_processed=len(df),
    status="SUCCESS"
)