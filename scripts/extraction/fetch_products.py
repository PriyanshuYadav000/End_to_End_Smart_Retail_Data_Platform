import requests
import pandas as pd

# API endpoint
url = "https://dummyjson.com/products?limit=200"

# Fetch data from API
response = requests.get(url)

# Convert response into JSON
data = response.json()

# Extract products list
products = data['products']

# Convert JSON to DataFrame
df = pd.DataFrame(products)

# Display first 5 rows
print(df.head())

# Save raw data
df.to_csv("data/raw/products_raw.csv", index=False)

print("Products data fetched successfully!")