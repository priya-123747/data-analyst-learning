
import pandas as pd

# ==========================================
# CREATE DATA
# ==========================================

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    "Sales": [50000, 5000, 8000, 30000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# ==========================================
# CSV
# ==========================================

# Save DataFrame as CSV

df.to_csv("sales_data.csv", index=False)

print("\nCSV file created successfully.")


# Read CSV

csv_data = pd.read_csv("sales_data.csv")

print("\nData Read From CSV:")
print(csv_data)


# ==========================================
# EXCEL
# ==========================================

# Save DataFrame as Excel

df.to_excel("sales_data.xlsx", index=False)

print("\nExcel file created successfully.")


# Read Excel

excel_data = pd.read_excel("sales_data.xlsx")

print("\nData Read From Excel:")
print(excel_data)

