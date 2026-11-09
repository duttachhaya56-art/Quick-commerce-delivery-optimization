import pandas as pd
import datetime

def check_raw_data(file_path):
    log_messages = []
    log_messages.append(f"--- Data Checkout Log: {datetime.datetime.now()} ---\n")
    
    # 1. load data
    try:
        df = pd.read_csv(file_path)
        msg1 = f"[SUCCESS] File loaded successfully: {file_path}"
        msg2 = f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}\n"
        print(msg1)
        print(msg2)
        log_messages.append(msg1)
        log_messages.append(msg2)
    except Exception as e:
        err_msg = f"[ERROR] Failed to load file: {e}"
        print(err_msg)
        log_messages.append(err_msg)
        return

    # 2. check for missing values
    missing_vals = df.isnull().sum()
    log_messages.append("--- Missing Values Check ---")
    print("--- Missing Values Check ---")
    for col, count in missing_vals.items():
        if count > 0:
            m_msg = f"[WARNING] Column '{col}' has {count} missing values"
            print(m_msg)
            log_messages.append(m_msg)

    # 3. check for duplicates rows
    duplicates = df.duplicated().sum()
    log_messages.append("\n--- Duplicate Check ---")
    print("--- Duplicate Check ---")
    if duplicates > 0:
        d_msg = f"[WARNING] Found {duplicates} duplicate rows in the dataset."
        print(d_msg)
        log_messages.append(d_msg)
    else:
        ok_msg = "[OK] No duplicate rows found."
        print(ok_msg)
        log_messages.append(ok_msg)

    # 4. save to a log file
    log_filename = "data_checkout_log.txt"
    with open(log_filename, "w") as log_file:
        log_file.write("\n".join(log_messages))
        
    print(f"\nData checkout complete! Log saved to {log_filename}")
    print("\nFirst 3 Rows of Data:")
    print(df.head(3))

# Yahan file path exact daal diya hai
check_raw_data("archive (2)/E-commerce_Delivery_Shipping_Data_2026.csv")
 