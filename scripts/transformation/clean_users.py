import pandas as pd
from scripts.utils.logger import log_etl_run


df = pd.read_csv("data/raw/users_raw.csv")

print("Raw Users Shape:", df.shape) 



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

print(df.columns)


df['full_name'] = df['firstname'] + " " + df['lastname']


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


df.to_csv("data/processed/users_cleaned.csv", index=False)

print("Users data cleaned successfully!")
print(df.head())

log_etl_run(
    pipeline_name="Users_Transformation",
    records_processed=len(df),
    status="SUCCESS"
)