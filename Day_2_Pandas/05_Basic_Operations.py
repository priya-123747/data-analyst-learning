
import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Sales": [50000, 5000, 8000, 30000, 15000],
    "Quantity": [5, 20, 15, 10, 8]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# Total Sales

print("\nTotal Sales:")
print(df["Sales"].sum())


# Average Sales

print("\nAverage Sales:")
print(df["Sales"].mean())


# Maximum Sales

print("\nMaximum Sales:")
print(df["Sales"].max())


# Minimum Sales

print("\nMinimum Sales:")
print(df["Sales"].min())


# Number of records

print("\nNumber of Records:")
print(df["Sales"].count())


# Total Quantity

print("\nTotal Quantity:")
print(df["Quantity"].sum())


# Add Profit column

df["Profit"] = df["Sales"] * 0.20

print("\nData with Profit:")
print(df)


# Sort by Sales

print("\nSorted by Sales:")
print(df.sort_values("Sales"))


# Sort in descending order

print("\nSales in Descending Order:")
print(df.sort_values("Sales", ascending=False))


# Statistical summary

print("\nStatistical Summary:")
print(df.describe())
