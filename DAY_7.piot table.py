import pandas as pd

df = pd.read_csv("Sales_Data.csv")

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Product",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)

print("Sales Pivot Table:")
print(pivot)
