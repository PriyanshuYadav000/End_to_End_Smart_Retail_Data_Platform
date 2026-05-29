import requests
import pandas as pd

# API endpoint
url = "https://dummyjson.com/products/categories"

# Fetch data
response = requests.get(url)

# Convert JSON
categories = response.json()

# Convert to DataFrame
df = pd.DataFrame(categories)

# Save raw data
df.to_csv("data/raw/categories_raw.csv", index=False)

print(df.head())
print("Categories data fetched successfully!")