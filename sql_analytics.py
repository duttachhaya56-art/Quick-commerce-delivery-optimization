import pandas as pd
import sqlite3

# 1. Dataset load karna
file_path = "archive (2)/E-commerce_Delivery_Shipping_Data_2026.csv"
df = pd.read_csv(file_path)

# 2. Local SQLite database connection banana
db_name = "quick_commerce_analytics.db"
conn = sqlite3.connect(db_name)

# 3. Data ko SQL table mein push karna (Data Modeling & Storage)
df.to_sql("quick_commerce_orders", conn, if_exists="replace", index=False)
print("--- DATABASE & TABLE CREATED SUCCESSFULLY ---")

# 4. Advanced SQL Query 1: Dark Store Bottleneck & Processing Time Analysis
query_bottleneck = """
    SELECT 
        delivery_status, 
        COUNT(*) as total_orders,
        ROUND(AVG(warehouse_processing_hours), 2) as avg_processing_hrs,
        ROUND(AVG(distance_km), 2) as avg_distance_km,
        ROUND(AVG(customer_rating), 2) as avg_customer_rating
    FROM quick_commerce_orders
    GROUP BY delivery_status
    ORDER BY avg_processing_hrs DESC;
"""

result_bottleneck = pd.read_sql(query_bottleneck, conn)
print("\n[SQL Query Result 1] Bottleneck Analysis by Delivery Status:")
print(result_bottleneck.to_string(index=False))

# 5. Advanced SQL Query 2: Order Priority wise SLA & Delay Risk Segmentation
query_priority = """
    SELECT 
        order_priority,
        delivery_status,
        COUNT(*) as order_count,
        ROUND(AVG(warehouse_processing_hours), 2) as avg_processing_time
    FROM quick_commerce_orders
    GROUP BY order_priority, delivery_status
    ORDER BY order_priority, order_count DESC;
"""

result_priority = pd.read_sql(query_priority, conn)
print("\n[SQL Query Result 2] Priority-wise Status Segmentation:")
print(result_priority.to_string(index=False))

# Connection close karna
conn.close()