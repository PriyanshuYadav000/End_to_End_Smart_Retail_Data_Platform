import requests
import pandas as pd


url = "https://dummyjson.com/products/categories"


response = requests.get(url)


categories = response.json()


df = pd.DataFrame(categories)


df.to_csv("data/raw/categories_raw.csv", index=False)

print(df.head())
print("Categories data fetched successfully!")