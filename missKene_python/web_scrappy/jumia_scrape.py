import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.com.ng/phones-tablets/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("article", class_="prd")

file = open("jumia_phones_tablets.txt", "w", encoding="utf-8")

written = 0

for product in products:
    name_tag = product.find("h3", class_="name")
    price_tag = product.find("div", class_="prc")
    old_price_tag = product.find("div", class_="old")
    discount_tag = product.select_one(".bdg._dsct")
    rating_tag = product.select_one(".stars._s")
    
    name = name_tag.text.strip() if name_tag else None
    price = price_tag.text.strip() if price_tag else None
    old_price = old_price_tag.text.strip() if old_price_tag else "N/A"
    discount = discount_tag.text.strip() if discount_tag else "N/A"
    rating = rating_tag.text.strip().split(" out")[0] if rating_tag else "N/A"

    if not name or not price:
        continue

    file.write(f"{name} | {price} | old: {old_price} | discount: {discount} | rating: {rating}\n")
    written += 1

print(f"{len(products)} products found, written {written} entries to file.")
file.close()
