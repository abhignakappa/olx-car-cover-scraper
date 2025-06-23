import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.olx.in/items/q-car-cover"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Collect results
items = soup.find_all("li", class_="EIR5N")

# Save to CSV
with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Location", "Link"])
    for item in items:
        title = item.find("span", class_="IKo3_")
        price = item.find("span", class_="_89yzn")
        location = item.find("span", class_="tjgMj")
        link = item.a['href'] if item.a else "N/A"
        writer.writerow([
            title.text if title else "N/A",
            price.text if price else "N/A",
            location.text if location else "N/A",
            "https://www.olx.in" + link
        ])
