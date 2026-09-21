import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
df = pd.read_csv("Sales_Data.csv")

# Sales by Product
product_sales = df.groupby("Product")["Sales"].sum()

product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
