import requests
import pandas as pd


url = "https://dummyjson.com/users?limit=200"


response = requests.get(url)


data = response.json()


users = data['users']


df = pd.DataFrame(users)


df.to_csv("data/raw/users_raw.csv", index=False)

print(df.head())
print("Users data fetched successfully!")