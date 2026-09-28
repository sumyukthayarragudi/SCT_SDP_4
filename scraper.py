import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Product Name", "Price", "Rating"])

    for page in range(1, 6):
        url = base_url.format(page)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("article", class_="product_pod")

        for product in products:
            name = product.h3.a["title"]
            price = product.find("p", class_="price_color").text
            rating = product.find("p", class_="star-rating")["class"][1]

            writer.writerow([name, price, rating])

print("Data successfully saved to products.csv")