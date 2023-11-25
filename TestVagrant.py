Bast = [
    {"product": "Leather wallet",
     "price": 1100,
     "GST": 18,
     "quantity": 1},
    {"product": "Umbrella",
     "price": 900,
     "GST": 12,
     "quantity": 4},
    {"product": "Cigarette",
     "price": 200,
     "GST": 28,
     "quantity": 3},
    {"product": "Honey",
     "price": 100,
     "GST": 0,
     "quantity": 2},
]
max_gst_product = max(Bast, key=lambda x: x["price"] * x["GST"] / 100 * x['quantity'])
min_gst_product = min(Bast, key=lambda x: x["price"] * x["GST"] / 100 * x['quantity'])
print("Product with maximum GST amount:", max_gst_product["product"])
print("Product with minimum GST amount:", min_gst_product["product"])
Total = sum((item["price"] * (1 + item["GST"] / 100)) * item["quantity"]
            for item in Bast)

# Apply a 5% discount for products with a unit price of Rs 500 or more
Discounted = sum(item["price"] * item["quantity"] * 0.95
            if item["price"] >= 500
            else item["price"] * item["quantity"]
            for item in Bast)

print("Amount to be paid (before discount): Rs", Total)
print("Amount to be paid (after 5% discount): Rs", Discounted)
