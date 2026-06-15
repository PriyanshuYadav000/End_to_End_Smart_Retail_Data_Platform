import pandas as pd
import ast

# Read raw carts file
df = pd.read_csv("data/raw/carts_raw.csv")

cart_items = []

for _, row in df.iterrows():

    cart_id = row["id"]

    products = ast.literal_eval(row["products"])

    for product in products:

        cart_items.append({
            "cart_id": cart_id,
            "product_id": product["id"],
            "product_title": product["title"],
            "price": product["price"],
            "quantity": product["quantity"],
            "item_total": product["total"],
            "discounted_total": product["discountedTotal"]
        })

fact_cart_items = pd.DataFrame(cart_items)

print(fact_cart_items.head())
print("Rows:", len(fact_cart_items))

fact_cart_items.to_csv(
    "data/processed/fact_cart_items.csv",
    index=False
)

print("fact_cart_items.csv created successfully!")