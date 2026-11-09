import pandas as pd

# data load kro
file_path = "archive (2)/E-commerce_delivery_shipping_data_2026.csv"
df = pd.read_csv(file_path)

# Clean CSV export krna power BI k liye
df.to_csv("quick_commerce_cleaned.csv", index=False)
print("Cleaned data successfully exported as 'quick_commerce_cleaned.csv' for power BI!")