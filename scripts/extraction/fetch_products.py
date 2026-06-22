import requests
import pandas as pd


url = "https://dummyjson.com/products?limit=200"


response = requests.get(url)


data = response.json()


products = data['products']


df = pd.DataFrame(products)


print(df.head())


df.to_csv("data/raw/products_raw.csv", index=False)

print("Products data fetched successfully!")