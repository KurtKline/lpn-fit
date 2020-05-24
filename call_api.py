import requests
import pandas as pd
import json

response = requests.get("http://127.0.0.1:8000/points/player/Kurt%20Kline")
response_json = response.json()

# See what it looks like, nicely.
print(json.dumps(response_json, indent=4))

# Load json into DataFrame
df = pd.DataFrame(response_json)
print(df)
