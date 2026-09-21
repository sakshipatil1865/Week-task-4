import pandas as pd

# Load sales data
df = pd.read_csv("Sales_Data.csv")

# Display data
print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Convert Sales and Quantity to numeric
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

print("\nFinal Data:")
print(df)

print("\nFinal Data Types:")
print(df.dtypes)
