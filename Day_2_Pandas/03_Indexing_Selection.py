
import pandas as pd

data = {
    "Employee": ["Arun", "Bala", "Priya", "Kumar", "Divya"],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

df = pd.DataFrame(data)

# 1. Select one column

print("Employee Column:")
print(df["Employee"])


# 2. Select multiple columns

print("\nEmployee and Salary:")
print(df[["Employee", "Salary"]])


# 3. Select first row

print("\nFirst Row:")
print(df.iloc[0])


# 4. Select first three rows

print("\nFirst Three Rows:")
print(df.iloc[0:3])


# 5. Select second and third rows

print("\nSecond and Third Rows:")
print(df.iloc[1:3])


# 6. Employees with salary greater than 50000

print("\nSalary Greater Than 50000:")
print(df[df["Salary"] > 50000])


# 7. Employees from IT department

print("\nIT Employees:")
print(df[df["Department"] == "IT"])


# 8. Employees with salary less than 50000

print("\nSalary Less Than 50000:")
print(df[df["Salary"] < 50000])


# 9. IT employees with salary greater than 50000

print("\nIT Employees with Salary Greater Than 50000:")
print(df[(df["Department"] == "IT") & (df["Salary"] > 50000)])

