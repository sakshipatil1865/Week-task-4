import requests
import pandas as pd

print("========== DAY 2: DATA COLLECTION FROM APIs ==========")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("\n========== API RESPONSE ==========")
print("Status Code:", response.status_code)

data = response.json()

# Convert API data into DataFrame
api_data = []

for user in data:
    api_data.append({
        "Name": user["name"],
        "Email": user["email"],
        "City": user["address"]["city"]
    })

df = pd.DataFrame(api_data)

print("\n========== API DATA TABLE ==========")
print(df.to_string(index=False))
