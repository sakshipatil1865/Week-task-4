import pandas as pd

df = pd.read_csv("Sales_Data.csv")

print("Total Sales:")
print(df["Sales"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nHighest Sales:")
print(df["Sales"].max())

print("\nLowest Sales:")
print(df["Sales"].min())

print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())

print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nBusiness Insights:")

highest_product = df.groupby("Product")["Sales"].sum().idxmax()
print("Highest selling product:", highest_product)

highest_region = df.groupby("Region")["Sales"].sum().idxmax()
print("Highest sales region:", highest_region)

highest_sale = df["Sales"].max()
print("Highest individual sale:", highest_sale)

lowest_sale = df["Sales"].min()
print("Lowest individual sale:", lowest_sale)
