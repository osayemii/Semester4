import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)

# file = open("scrape1.html", "w", encoding="utf-8")
# file.write(response.text)
# file.close()

print(response.status_code)
print(response.text)