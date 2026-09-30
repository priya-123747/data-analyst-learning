
import pandas as pd

# ==========================================
# MERGE
# ==========================================

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Name": ["Arun", "Bala", "Priya"]
})

salary = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Salary": [50000, 45000, 60000]
})

print("Employees:")
print(employees)

print("\nSalary:")
print(salary)


# Merge

merged = pd.merge(
    employees,
    salary,
    on="Employee_ID"
)

print("\nMerged Data:")
print(merged)


# ==========================================
# CONCATENATE
# ==========================================

df1 = pd.DataFrame({
    "Name": ["Arun", "Bala"],
    "Department": ["IT", "HR"]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Kumar"],
    "Department": ["Sales", "IT"]
})

print("\nDataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)


combined = pd.concat([df1, df2])

print("\nConcatenated Data:")
print(combined)


# ==========================================
# JOIN
# ==========================================

employees = pd.DataFrame({
    "Name": ["Arun", "Bala", "Priya"]
}, index=[101, 102, 103])

salary = pd.DataFrame({
    "Salary": [50000, 45000, 60000]
}, index=[101, 102, 103])

joined = employees.join(salary)

print("\nJoined Data:")
print(joined)
