
import pandas as pd

# ==========================================
# DAY 2 - PANDAS
# TOPIC: SERIES
# DOMAIN: DATA ANALYST
# ==========================================


# 1. Creating a simple Series

sales = pd.Series([5000, 7000, 4500, 9000, 6500])

print("Sales Series:")
print(sales)


# 2. Creating a Series with custom index

sales = pd.Series(
    [5000, 7000, 4500, 9000, 6500],
    index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
)

print("\nSales with Days:")
print(sales)


# 3. Accessing one value

print("\nMonday Sales:")
print(sales["Monday"])


# 4. Accessing multiple values

print("\nMonday and Wednesday Sales:")
print(sales[["Monday", "Wednesday"]])


# 5. Accessing value using position

print("\nFirst Sales Value:")
print(sales.iloc[0])


# 6. Accessing multiple values using position

print("\nFirst Three Sales Values:")
print(sales.iloc[0:3])


# 7. Finding total sales

print("\nTotal Sales:")
print(sales.sum())


# 8. Finding average sales

print("\nAverage Sales:")
print(sales.mean())


# 9. Finding maximum sales

print("\nMaximum Sales:")
print(sales.max())


# 10. Finding minimum sales

print("\nMinimum Sales:")
print(sales.min())


# 11. Finding number of values

print("\nNumber of Sales Records:")
print(sales.count())


# 12. Finding the index

print("\nIndex:")
print(sales.index)


# 13. Finding the values

print("\nValues:")
print(sales.values)


# 14. Checking the data type

print("\nData Type:")
print(sales.dtype)


# 15. Basic statistical information

print("\nStatistical Summary:")
print(sales.describe())

