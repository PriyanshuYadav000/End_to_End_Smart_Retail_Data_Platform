import pandas as pd
from scripts.utils.logger import log_etl_run

# Read raw users data
df = pd.read_csv("data/raw/users_raw.csv")

print("Raw Users Shape:", df.shape) 
# print Raw Users Shape: (30, 28)

# Remove duplicates
df = df.drop_duplicates()

# Fill numeric null values
numeric_cols = df.select_dtypes(include='number').columns
# print("Numeric Columns:", numeric_cols)

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill text null values
text_cols = df.select_dtypes(include=['object', 'string']).columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print(df.columns)

# Create full name
df['full_name'] = df['firstname'] + " " + df['lastname']

# Select important columns
selected_columns = [
    'id',
    'full_name',
    'age',
    'gender',
    'email',
    'phone',
    'username',
    'birthdate',
    'bloodgroup',
    'university',
    'role'
]

df = df[selected_columns]

# Save cleaned users data
df.to_csv("data/processed/users_cleaned.csv", index=False)

print("Users data cleaned successfully!")
print(df.head())

log_etl_run(
    pipeline_name="Users_Transformation",
    records_processed=len(df),
    status="SUCCESS"
)