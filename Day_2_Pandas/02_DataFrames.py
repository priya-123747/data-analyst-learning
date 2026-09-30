
import pandas as pd

# ==========================================
# DAY 2 - PANDAS
# TOPIC: DATAFRAMES
# DOMAIN: DATA ANALYST
# ==========================================

# 1. Creating a DataFrame

data = {
    "Employee": ["Arun", "Bala", "Priya", "Kumar", "Divya"],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


# 2. Display first rows

print("\nFirst 3 rows:")
print(df.head(3))


# 3. Display last rows

print("\nLast 2 rows:")
print(df.tail(2))


# 4. Display column names

print("\nColumn Names:")
print(df.columns)


# 5. Display number of rows and columns

print("\nShape:")
print(df.shape)


# 6. Display DataFrame information

print("\nDataFrame Information:")
print(df.info())


# 7. Display one column

print("\nEmployee Names:")
print(df["Employee"])


# 8. Display multiple columns

print("\nEmployee and Salary:")
print(df[["Employee", "Salary"]])


# 9. Display first row

print("\nFirst Row:")
print(df.iloc[0])


# 10. Display second row

print("\nSecond Row:")
print(df.iloc[1])


# 11. Display first three rows

print("\nFirst Three Rows:")
print(df.iloc[0:3])


# 12. Add a new column

df["Bonus"] = df["Salary"] * 0.10

print("\nDataFrame with Bonus:")
print(df)


# 13. Find average salary

print("\nAverage Salary:")
print(df["Salary"].mean())


# 14. Find highest salary

print("\nHighest Salary:")
print(df["Salary"].max())


# 15. Find lowest salary

print("\nLowest Salary:")
print(df["Salary"].min())

