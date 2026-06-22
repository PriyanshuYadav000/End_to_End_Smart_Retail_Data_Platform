import pandas as pd
from scripts.utils.logger import log_etl_run


df = pd.read_csv("data/raw/categories_raw.csv")

print("Raw Categories Shape:", df.shape)


df = df.drop_duplicates()


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


df.to_csv("data/processed/categories_cleaned.csv", index=False)

print("Categories cleaned successfully!")
print(df.head())

log_etl_run(
    pipeline_name="Categories_Transformation",
    records_processed=len(df),
    status="SUCCESS"
)