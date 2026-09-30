
import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Employee": ["Arun", "Priya", "Bala", "Divya", "Kumar", "Ravi"],
    "Salary": [50000, 60000, 45000, 48000, 55000, 65000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# 1. Average salary by department

print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())


# 2. Total salary by department

print("\nTotal Salary by Department:")
print(df.groupby("Department")["Salary"].sum())


# 3. Maximum salary by department

print("\nMaximum Salary by Department:")
print(df.groupby("Department")["Salary"].max())


# 4. Minimum salary by department

print("\nMinimum Salary by Department:")
print(df.groupby("Department")["Salary"].min())


# 5. Count employees by department

print("\nEmployee Count by Department:")
print(df.groupby("Department")["Employee"].count())


# 6. Multiple aggregation operations

print("\nMultiple Aggregations:")
print(
    df.groupby("Department")["Salary"].agg(
        ["sum", "mean", "max", "min"]
    )
)
