
import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Salary": [50000, 60000, 45000, 48000, 55000, 65000]
}

df = pd.DataFrame(data)

print(df)


# Sum

print("\nTotal Salary:")
print(df["Salary"].sum())


# Mean

print("\nAverage Salary:")
print(df["Salary"].mean())


# Median

print("\nMedian Salary:")
print(df["Salary"].median())


# Maximum

print("\nMaximum Salary:")
print(df["Salary"].max())


# Minimum

print("\nMinimum Salary:")
print(df["Salary"].min())


# Count

print("\nEmployee Count:")
print(df["Salary"].count())


# Complete statistical summary

print("\nStatistical Summary:")
print(df["Salary"].describe())

