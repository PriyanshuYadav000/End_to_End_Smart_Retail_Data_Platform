import requests
import pandas as pd

# API endpoint
url = "https://dummyjson.com/carts?limit=200"

# Fetch data
response = requests.get(url)

# Convert JSON
data = response.json()

# Extract carts
carts = data['carts']

# Convert to DataFrame
df = pd.DataFrame(carts)

# Save raw data
df.to_csv("data/raw/carts_raw.csv", index=False)

print(df.head())
print("Carts data fetched successfully!")