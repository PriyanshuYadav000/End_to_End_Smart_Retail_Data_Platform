import requests
import pandas as pd


url = "https://dummyjson.com/carts?limit=200"


response = requests.get(url)


data = response.json()


carts = data['carts']


df = pd.DataFrame(carts)


df.to_csv("data/raw/carts_raw.csv", index=False)

print(df.head())
print("Carts data fetched successfully!")