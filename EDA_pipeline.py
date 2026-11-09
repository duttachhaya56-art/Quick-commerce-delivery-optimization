import pandas as pd

# Data load karo
file_path = "archive (2)/E-commerce_Delivery_Shipping_Data_2026.csv"
df = pd.read_csv(file_path)

print("--- DEEP-DIVE QUICK-COMMERCE BOTTLENECK ANALYSIS ---")

# 1. Delivery Status ke hisaab se average Warehouse Processing Hours
print("\n[1] Average Warehouse Processing Hours by Delivery Status:")
if 'warehouse_processing_hours' in df.columns and 'delivery_status' in df.columns:
    processing_impact = df.groupby('delivery_status')['warehouse_processing_hours'].mean().reset_index()
    print(processing_impact.to_string(index=False))

# 2. Distance vs Delivery Status Analysis
print("\n[2] Average Delivery Distance (km) by Delivery Status:")
if 'distance_km' in df.columns and 'delivery_status' in df.columns:
    distance_impact = df.groupby('delivery_status')['distance_km'].mean().reset_index()
    print(distance_impact.to_string(index=False))

# 3. Customer Rating Impact on Delayed vs Delivered orders
print("\n[3] Average Customer Rating by Delivery Status:")
if 'customer_rating' in df.columns and 'delivery_status' in df.columns:
    rating_impact = df.groupby('delivery_status')['customer_rating'].mean().reset_index()
    print(rating_impact.to_string(index=False))

print("\n--- EDA Deep-Dive Completed Successfully! ---")