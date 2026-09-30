
import pandas as pd

data = {
    "Employee": ["Arun", "Bala", "Priya", "Kumar", "Divya"],
    "Salary": [50000, None, 60000, None, 48000],
    "Age": [25, 28, None, 30, 26]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# 1. Check missing values

print("\nMissing Values:")
print(df.isnull())


# 2. Count missing values

print("\nMissing Value Count:")
print(df.isnull().sum())


# 3. Remove rows containing missing values

print("\nAfter dropna:")
print(df.dropna())


# 4. Fill missing Salary with 0

df["Salary"] = df["Salary"].fillna(0)

print("\nSalary after fillna:")
print(df)


# 5. Fill missing Age with average age

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAge after filling with average:")
print(df)

