import requests

url = "https://books.toscrape.com"
response = requests.get(url)

print(f"Status code: {response.status_code}")