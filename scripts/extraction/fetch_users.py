import requests
import pandas as pd

# API endpoint
url = "https://dummyjson.com/users?limit=200"

# Fetch data
response = requests.get(url)

# Convert to JSON
data = response.json()

# Extract users
users = data['users']

# Convert to DataFrame
df = pd.DataFrame(users)

# Save raw data
df.to_csv("data/raw/users_raw.csv", index=False)

print(df.head())
print("Users data fetched successfully!")