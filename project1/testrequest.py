import requests

url = "http://127.0.0.1:5000/generate"
payload = {"description": "def add(a, b):\n    "}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
