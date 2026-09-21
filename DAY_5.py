import pandas as pd

df = pd.read_csv("Sales_Data.csv")

print("Dataset:")
print(df)

print("\nBasic Statistics:")
print(df.describe())

print("\nProduct Count:")
print(df["Product"].value_counts())

print("\nRegion Count:")
print(df["Region"].value_counts())

print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())
