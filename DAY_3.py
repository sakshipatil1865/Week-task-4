import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("sales.db")

# Create table
query = """
CREATE TABLE IF NOT EXISTS sales (
    Product TEXT,
    Region TEXT,
    Sales INTEGER,
    Quantity INTEGER
)
"""

conn.execute(query)

# Insert sales data
data = [
    ("Laptop", "West", 50000, 1),
    ("Mobile", "South", 70000, 3),
    ("Mouse", "North", 45000, 2),
    ("Tablet", "East", 20000, 1),
    ("Printer", "West", 35000, 2)
]

conn.executemany(
    "INSERT INTO sales VALUES (?, ?, ?, ?)", data
)

conn.commit()

# Read data using Pandas
df = pd.read_sql("SELECT * FROM sales", conn)

print(df)

conn.close()
