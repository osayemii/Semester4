import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article", class_="product_pod")

# file = open("file.txt", "w", encoding='utf-8')

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    
    # file.write(f"{title} - {price}\n")
    
    print(f"{title} - {price}")

# file.close()